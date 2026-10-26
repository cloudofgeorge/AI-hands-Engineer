# C/C++ bug-class reference

Adapted from Trail of Bits c-review. Read the relevant entries during the location-based review, then sweep applicable classes not yet covered. Platform and threat-model exclusions must be supported by source evidence.

## buffer-overflow — Out-of-bounds write

Spatial safety at any write: index arithmetic, loop bounds, size computations that reach a fixed or heap buffer. The high-yield shape is a size that is computed correctly for one buffer and used against another, or a bound that is re-derived rather than reused. Not a finding when the index is provably constrained at every caller; say where.

## oob-read — Out-of-bounds read

A read past either end of an allocation, which `buffer-overflow` does not cover — that class is explicitly the out-of-bounds *write*. The shapes: an index validated against the wrong buffer's length, a loop that reads one element past its bound, a length taken from the data rather than from the allocation, and back-references or window offsets in a decompressor that point behind the start of the buffer. Impact is disclosure or a crash, so it is a real vulnerability even where nothing is written.

## memcpy-size — Bad size argument to a memory primitive

The third argument to memcpy/memmove/memset/bcopy. Signed subtraction that can go negative then converts to a huge size_t; a syscall return used without an error check; unsigned subtraction that wraps. sizeof on a pointer rather than the pointee is the classic silent one.

## overlapping-buffers — Overlapping source and destination

memcpy, strcpy, sprintf and the str*cat family are undefined when the regions overlap; only memmove is defined. Aliasing usually arrives through two pointers into the same allocation (buf and buf+k), not through a literally identical argument.

Candidate-site evidence: memcpy or strcpy with two pointers derived from one allocation

## flexible-array — Flexible-array / struct-hack sizing

A trailing data[0] or data[1] member sized with sizeof(struct) rather than offsetof(struct, data) allocates one element too few or too many. The [1] form is the dangerous one: sizeof already counts the element, so the arithmetic silently disagrees with the C99 data[] form other code assumes.

Candidate-site evidence: a struct whose last member is an array of length 0 or 1

## string-bounds-and-termination — String bounds and NUL termination

The three classic C string sizing errors, which are one bug with three faces. malloc(strlen(s)) followed by strcpy writes one byte past the allocation — only a bug when the destination is later used as a C string, since a raw copy of exactly strlen bytes is fine. strncpy does not NUL-terminate when the source is at least n bytes, so look for the missing buf[n-1] = 0 and for that assignment existing on only one branch. strncat's third argument is how many bytes to APPEND, not the destination size, and it always writes one more byte for the NUL, so sizeof(dst) is wrong by strlen(dst)+1; that one is almost always a real overflow when it appears.

Candidate-site evidence: a call to strcpy, strncpy, strncat, or an allocation sized from strlen

## string-issues — Encoding, locale and multibyte handling

Byte length confused with character length across a conversion boundary; locale-dependent case folding used for a security comparison (Turkish dotless i is the standing example); missing UTF-8/UTF-16 validation where downstream code assumes well-formed input; surrogate-pair and overlong-encoding handling. Encoding-invariant violations are a real vulnerability class in parsers, not a cosmetic issue.

Candidate-site evidence: multibyte, wide-character, locale or encoding-validation code

## format-string — Format-string control

A non-literal format argument anywhere in the printf/syslog family, %n as a write primitive, and argument/specifier type mismatches. Also variadic wrappers that forward to v*printf without __attribute__((format)), which turns off every compiler check at every call site.

Candidate-site evidence: a printf/syslog-family call, or a variadic wrapper forwarding to v*printf

## snprintf-retval — snprintf return value is the would-have-been length

snprintf returns the length the output WOULD have had, which can exceed the buffer size; it is not the number of bytes written. So buf[n] = 0 with n from the return can write out of bounds, ptr += snprintf(...) can run the pointer past the end, and remaining = size - snprintf(...) can go negative. asprintf returns -1 and leaves the pointer indeterminate on failure.

Candidate-site evidence: a call to snprintf, vsnprintf or asprintf whose return value is used

## scanf-uninit — scanf family leaves targets uninitialized

On a partial or failed match the *scanf family leaves later targets untouched, so an uninitialized local is read as if parsed. The return value is the number of items assigned; ignoring it is what makes this exploitable. %s with no field width is a separate unbounded write.

Candidate-site evidence: a call to scanf, sscanf or fscanf

## banned-api-with-attacker-data — Banned or discouraged API reached by attacker data

gets, strcpy, strcat, sprintf, vsprintf, tmpnam, tempnam, mktemp, strtok, alloca, putenv, rand for security purposes, width-less %s conversions, stpcpy, atoi and friends with no error channel. THE EVIDENCE BAR IS A FLOW, NOT A NAME: report one of these as a vulnerability only when you can trace attacker-influenced data or an attacker-influenced size to it, and state the source, the sink and what validates between them. A call whose inputs are provably bounded internal constants is a hardening observation, not a vulnerability — you may still report it, but say so plainly in the impact so the judge can rate it accordingly. Check for a project-local macro or wrapper shadowing the libc name before concluding anything.

Candidate-site evidence: a call to one of the banned functions named in this brief

## uninitialized-data — Use or disclosure of uninitialized memory

Locals read on a path that skips their assignment, structs serialized with padding bytes intact, arrays partially filled then used at full length. The disclosure half matters as much as the use half: struct padding and tail bytes leaked over a socket or into a file are an information leak even when nothing misbehaves.

## null-deref — Null pointer dereference

Unchecked allocation returns and unchecked lookup failures. The subtle variant is a check placed after a dereference: the compiler is entitled to delete the check because the earlier dereference already proved the pointer non-null, so the guard you can see is not the guard that runs.

Candidate-site evidence: an allocation or lookup whose result is dereferenced

## use-after-free — Use after free, double free, dangling pointer

A pointer that survives its allocation: freed on an error path and used by the caller, freed twice through two owners, or invalidated by a realloc whose old value some other variable still holds. Realloc aliasing is the one most often missed — every copy of the old pointer is dangling after a successful realloc.

## memory-leak — Memory and resource leak

Leaks matter here when the leaking path is attacker-repeatable — an error branch reachable from untrusted input is a remote memory-exhaustion primitive. A leak only reachable once at startup is not. File descriptors, sockets and locks count as resources. Cold error paths are where these live, and cold error paths are the ground an attacker-reachability prior deprioritises, so read them deliberately.

## state-field-invariant — Invariant on a field of a shared state struct

A field or flag of a long-lived struct carries a rule that must hold across every reset, allocation, refill and free path, and one path breaks it. C-specific by construction: malloc does not zero, lifetime is manual, and the struct is threaded through a state machine where no single function owns the field. A broken invariant here can present under any symptom label, so a class label you grep for will not surface it. THIS IS NOT A LABEL TO GREP FOR. It is the output of the invariant audit: enumerate the fields, find every writer and every reader, and prove the field's rule at each. Used as a search term it will reproduce the failure it was created to describe.

## integer-overflow — Integer overflow, truncation and signedness

Size and length arithmetic is the payload: n * sizeof(T) with no overflow check, a + b compared against a bound after the addition already wrapped, a 64-bit length truncated into an int, a signed value that goes negative and then converts to a huge size_t. Signed overflow is undefined, so a post-hoc check like if (a + b < a) may be deleted by the compiler — that is a bug even where the wrap would have been benign. Growth patterns that double a size, or add a header to a body length, are where this reaches memory corruption. Unsigned subtraction is the quiet one: `a - b` where b can exceed a wraps to a near-SIZE_MAX value that passes every upper-bound check written for the non-wrapping case.

## oob-comparison — Comparison reads past the shorter buffer

memcmp/strncmp/bcmp with a length taken from the longer operand, and the three-iterator std::equal, which reads from the second range without knowing its end. Also: memcmp is not constant-time, so using it on a secret is a separate timing problem worth noting.

Candidate-site evidence: a call to memcmp, strncmp, bcmp or std::equal

## operator-precedence — Operator precedence and associativity

Shift binds looser than addition; bitwise and/or bind looser than comparison; the ternary binds looser than assignment. The security-relevant shapes are a mask test written without parentheses and a size expression whose intended grouping differs from the parsed one.

## type-confusion — Type confusion, unsafe casts and null/zero conversions

A buffer cast to a struct larger than the allocation is the memory-corrupting form — look for numbered or "extended" struct variants where the choice of variant comes from the data. Also: union members read under the wrong tag, void* callback payloads cast back to the wrong type, and C++ downcasts done with static_cast where the dynamic type is attacker-influenced. In a variadic (or K&R) call the compiler cannot convert 0 to a null pointer, so execl(path, arg, 0) passes an int where a char* terminator is required, and on LP64 that is 32 bits of zero followed by whatever is next; 0 in a prototyped pointer parameter is fine.

## undefined-behavior — Undefined behavior the optimizer can weaponize

Shifts by a negative amount or by at least the promoted width; misaligned loads via a cast; strict-aliasing violations that are not char*, memcpy or a union; unsequenced modification of the same object. What makes these security bugs rather than pedantry is that the optimizer is allowed to assume they never happen and delete the surrounding check — so the consequences belong here too: memset of a secret before the object dies is dead-store-eliminated unless explicit_bzero, memset_s, SecureZeroMemory or a volatile access is used; security checks inside assert() vanish under NDEBUG; a null check placed after a dereference is removable; and constant-time code written in plain C is not constant-time after optimization.

## error-handling — Unchecked, mis-compared or mis-propagated return values

Ignoring the return of an allocation, an open, a crypto verify, or a write. Comparing against the wrong success convention — a function that returns 1 on success tested with != 0, or -1 on error tested with != 1. A failure that is logged but not propagated leaves the caller acting on invalid state. Three specific shapes travel with this class. NEGATIVE RETURNS: read/write/recv/send/snprintf return negative on error, and assigned into a size_t, -1 becomes SIZE_MAX, after which n == -1 against an unsigned type is never true — the check reads as present but never fires. ERRNO: it is only meaningful after a call that failed, functions with a legitimate sentinel (strtol returning 0 or LONG_MAX, getpwnam returning NULL) need errno = 0 before the call, and errno is clobbered by intervening library calls including the logging call in the error branch itself. EINTR: blocking syscalls must be retried unless SA_RESTART covers every installed handler, close() is the exception because on Linux the descriptor is already released when it returns EINTR so retrying can close an unrelated descriptor, and a retry loop that restarts a partial read from the beginning is also wrong.

## open-issues — Unsafe file open and path resolution

access() then open() is a symlink race whenever the directory is attacker-writable, and access() answers for the real uid, not the effective one. O_NOFOLLOW only refuses a symlink as the final component — every directory in the path is still followed; openat2 with RESOLVE_NO_SYMLINKS or component-by-component openat is the real fix. Missing O_CLOEXEC leaks descriptors across exec.

Candidate-site evidence: a call to open, openat, creat or access

Scope condition: POSIX APIs must be used.

## filesystem-issues — Symlink, temp file and path-normalization issues

Predictable temp names (tmpnam/tempnam/mktemp, or a PID-derived name) in a shared directory; a path prefix check that a "..", a symlink, a trailing slash, or a case-insensitive filesystem can defeat; Unicode normalization applied after the check rather than before. A prefix test that compares strings rather than resolved paths is the recurring bug.

Candidate-site evidence: temp-file creation, or a path prefix or traversal check

## socket-state — Socket association and half-closed state

Calling connect() with sa_family set to AF_UNSPEC dissolves an already-connected socket, after which it can be reconnected elsewhere; if any part of a sockaddr reaching connect() is attacker-influenced, the association a sandbox or a peer identity relies on can be dropped, and this has been used for sandbox escapes. Separately, shutdown(fd, SHUT_WR) leaves the socket readable and SHUT_RD leaves it writable, so a state machine that treats "peer closed" as "connection over" keeps processing data that arrives in the half-closed window, or frees per-connection state a subsequent read still touches — and a peer that half-closes rather than closing can hold a connection slot open indefinitely.

Candidate-site evidence: a call to connect, shutdown or a per-connection state machine

Scope condition: POSIX APIs must be used.

## race-condition — TOCTOU and unsynchronized shared state

Check-then-act on anything another actor can change between the two steps: a filesystem path, a shared counter, a cached pointer. Double-fetch is the memory version — reading an attacker-writable location twice and assuming the two reads agree, so the validated value is not the used value. Also lock scope that ends before the compound operation does.

Candidate-site evidence: threads, shared mutable globals, or a check-then-act on the filesystem

## thread-safety — Non-reentrant calls and uninitialized lock primitives

gethostbyname, inet_ntoa, strtok, strerror, localtime, gmtime, ctime, asctime, getpwnam, getgrnam and readdir return pointers to static storage that the next call from any thread overwrites; the bug is not the call, it is the window between the call and the consumption of the result. pthread_spinlock_t has no static initializer, so a spinlock reached on a path that skipped pthread_spin_init — or whose init return was ignored — is used uninitialized, and the same shape applies to a mutex whose pthread_mutex_init failed unchecked. Only relevant if the process actually creates threads.

Candidate-site evidence: pthread_create or another thread-creation API

Scope condition: POSIX APIs must be used.

## signal-handler — Async-signal-unsafe handler

A handler may call only async-signal-safe functions. malloc/free reentered from a handler corrupts the allocator; stdio reentered from a handler corrupts its lock and buffers; longjmp out of a handler leaves everything indeterminate. A handler must also save and restore errno. The safe shapes are: set a volatile sig_atomic_t flag, or write() one byte to a self-pipe.

Candidate-site evidence: a call to signal() or sigaction()

## access-control — Missing or misplaced authorization

An operation that changes state or returns data on behalf of a principal, with no check that the principal is entitled to it — or a check performed on a different value than the one used. Includes capability and descriptor leaks across a privilege boundary.

## privilege-drop — Incomplete or unchecked privilege drop

setuid() from a non-root effective uid can fail while returning a value nobody checks, leaving the process privileged. seteuid() alone leaves the saved-set-uid, so privileges can be regained; setresuid(uid,uid,uid) is the complete form. Groups must be dropped before the user, and setgroups() must be called to clear the supplementary set. Verify the drop by reading back the ids.

Candidate-site evidence: a call to setuid, seteuid, setresuid, setgid or setgroups

Scope condition: POSIX APIs must be used.

Scope condition: Normally outside a remote-only attacker model; justify applicability.

## envvar — Environment variable trust

Under LOCAL_UNPRIVILEGED the environment is attacker data. Relevant shapes: a privileged process trusting a variable for a path or a library location; a secret placed in the environment where any process that can read /proc/<pid>/environ sees it; setenv leaving the previous value reachable; a child inheriting an environment that was never sanitized.

Candidate-site evidence: a call to getenv, setenv or putenv

Scope condition: Normally outside a remote-only attacker model; justify applicability.

## time-issues — Clock and time-arithmetic assumptions

Wall-clock time used to measure a duration (an expiry or a rate limit that the clock stepping backwards defeats); 32-bit time_t overflow; comparisons that assume 86400-second days across a DST or leap-second boundary. Only report where the wrong answer has a security consequence.

Candidate-site evidence: a time(), gettimeofday() or clock call used for expiry or rate limiting

## dos — Attacker-controlled resource consumption

Unbounded allocation, unbounded recursion, and superlinear algorithms driven by input size. Recursion depth is the highest-yield one in parsers: look for a depth counter that exists but is never compared against a limit, a limit that only counts one of several recursive paths, or an amplification guard that a linear chain slips under. Hash-table collision floods and regex backtracking belong here too. A countable population — enumerate EVERY recursive construct before writing this class off; filing one stack-exhaustion bug does not cover the class: the same file can hold other recursive constructs.

## exploit-mitigations — Missing or silently misspelled hardening flags

Read the actual build files. The interesting failure is not an absent flag but a misspelled one — _FORTIFY_SORUCE, -fstack-protector-stong, _GLIBCXX_ASSERTONS — because a typo in a -D or a -f flag is accepted silently and the mitigation is simply off while the build looks hardened. Also check that the flag reaches the target, not only a sample or test build.

Candidate-site evidence: a Makefile, CMakeLists.txt, configure script or meson.build in the tree

## qsort — Non-transitive comparator drives qsort out of bounds

glibc qsort trusted its comparator to be a valid ordering; an inconsistent one walks the merge past the array (CVE-2023-6246 family, Qualys 2024). Inconsistency sources: subtracting ints, which overflows; comparing only a prefix or one field of a record; floating point where NaN makes every comparison false; and a multi-key comparator that returns 0 for distinct records. The safe form is (a > b) - (a < b).

Candidate-site evidence: a call to qsort, bsearch or another comparator-taking function

Scope condition: POSIX APIs must be used.

## regex-issues — Regex denial of service and matching bypasses

Backtracking blowup from nested or overlapping quantifiers on attacker input. Bypasses: an unanchored pattern used as if it were a whole-string test, and POSIX regexec matching per line unless REG_NEWLINE semantics are considered, so an embedded newline can hide the rest of the input from a check.

Candidate-site evidence: a call to regcomp, regexec or another regex API

## va-start-end — va_list lifecycle

Every va_start and every va_copy needs a matching va_end before the function returns, including on early-error paths. Reusing a va_list after it has been consumed by one v*printf call is undefined — a second consumer needs va_copy.

Candidate-site evidence: a va_start, va_copy or variadic function definition

## logic-flaw — Security logic, protocol and state-machine flaws

Everything memory-safety taxonomies do not name, and often the highest-yield class, because it catches logic bugs that fit no specific label below. Namespace or delimiter injection, where a separator character the format reserves is accepted inside a value and re-emitted so the two parse differently on the way back. Protocol state machines that accept a message in a state that skips authentication or size negotiation, or that return success on a path meant to signal "need more input". Deserialization that lets input choose a type or a size. Off-by-one in an index-to-identity mapping. Two named patterns worth hunting explicitly, because both were found here without a class of their own: VALIDATED-VALUE SUBSTITUTION, where one value is checked and a different, unchecked one reaches the sink — validation applied to a normalized copy while the raw value is used downstream is the same shape; and CALL-SITE INVARIANT, where a shared macro or helper enforces a well-formedness rule at some expansion sites and not all, so one path admits input the others reject. Also: a value read out of a header or a length field and stored into state without being checked against the bound the rest of the code assumes. These are found by reading what a value is ALLOWED to be and then asking what the code does with a value one step outside that.

## crypto-misuse — Cryptographic misuse

Correct primitives assembled wrongly. A nonce or IV reused across two messages under one key, or derived from a counter that resets when the process does. One key serving two purposes, or a long-term key used where an ephemeral one belongs. Secrets, MACs or tags compared with memcmp or strcmp, which returns early and leaks position. Ciphertext decrypted before its tag is checked, or a tag never checked. ECB, or any unauthenticated mode where the plaintext is attacker-influenced. Keys or salts from rand/srand, time, a PID, or a hardcoded constant instead of a CSPRNG. A KDF with no salt or a trivial iteration count. Padding or signature verification whose failure path returns the same value as success. Judge the construction against what the primitive requires of its caller, not against whether the primitive itself is sound.

Candidate-site evidence: a cryptographic primitive, key, nonce, MAC or random-number call

## smart-pointer — C++ smart pointer ownership

Two independent shared_ptr control blocks built from one raw pointer (double free); a raw pointer or reference handed out of a unique_ptr and outliving it; shared_ptr cycles; weak_ptr::lock() result used without checking.

## move-semantics — Use of a moved-from object

A moved-from object is valid but unspecified. The security-relevant shape is a buffer or key moved out and then read as if it still held the data, and a std::move inside a loop that moves the same object on every iteration.

## lambda-capture — Lambda capture outliving its referent

A lambda stored in a callback, a thread, or a coroutine that captured a local by reference, or captured this, and now outlives it. [=] on a member function captures this by value, not the members — a common surprise.

## iterator-invalidation — Iterator, pointer or reference invalidated by a container mutation

Any vector or string growth invalidates every iterator, pointer and reference into it, including one held across a function call that appends. Erasing inside a loop without taking the returned iterator. unordered_ containers invalidate iterators on rehash but keep references valid — the asymmetry causes real bugs.

## init-order — Static initialization order

A namespace-scope object in one translation unit whose constructor reads one defined in another has no defined order. Member initializers run in declaration order, not in the order they are written in the list. The observable failure is a security check reading a not-yet-initialized table.

## virtual-function — Virtual dispatch hazards

A virtual call in a constructor or destructor dispatches to the class being constructed, not the derived override, so a derived-class invariant check silently does not run. Deleting through a base pointer without a virtual destructor. Object slicing on assignment to a base value.

## exception-safety — Exception paths that leak or leave partial state

A resource acquired between a try and the RAII wrapper that would release it; a destructor that can throw (terminate during unwind); a noexcept function whose callee throws. The security shape is a lock or a privilege left held, or a half-updated invariant observed after the handler.

## createprocess — Windows process creation

An unquoted lpApplicationName/lpCommandLine path with spaces lets C:\Program.exe run instead of the intended target. bInheritHandles = TRUE hands every inheritable handle to the child. Also: creating a process with a token or a working directory the caller does not control.

## cross-process — Cross-process memory and handle access

OpenProcess/ReadProcessMemory/WriteProcessMemory against a PID that can be recycled or a handle obtained without verifying the target identity. Duplicating a handle into a lower-privileged process with more access than intended.

## token-privilege — Token and impersonation handling

Impersonation that is not reverted on every path, including error paths. ImpersonateNamedPipeClient without first checking the client is who is expected. Privileges enabled and left enabled. A SECURITY_DESCRIPTOR with a NULL DACL, which grants everyone full control (it is not the same as an empty DACL, which grants no one).

## service-security — Windows service configuration

A service binary or its directory writable by non-admins; a service whose ACL allows SERVICE_CHANGE_CONFIG to a non-admin (the binary path can then be rewritten); an unquoted ImagePath with spaces.

## dll-planting — DLL search-order hijacking

LoadLibrary with a bare name, or an implicit import of a DLL not present in System32, resolves through a search order that includes the application directory and (without SetDefaultDllDirectories) the current directory. Use a fully qualified path or LOAD_LIBRARY_SEARCH_SYSTEM32.

## windows-path — Windows path parsing

Path checks defeated by 8.3 short names, alternate data streams, a trailing dot or space that the filesystem strips, the \\?\ prefix that skips normalization, device names such as CON and NUL, and UNC paths reaching a check written for local paths. Case-insensitivity plus Unicode folding defeats string prefix tests.

## installer-race — Installer and updater filesystem race

A privileged installer writing to or executing from a directory a normal user can write, or extracting to a temp directory before setting its ACL. The window between create and ACL-set is the bug.

## named-pipe — Named pipe security

A server that does not create the pipe with FILE_FLAG_FIRST_PIPE_INSTANCE can be squatted by a client that created the name first. A server that impersonates a client without validating it, or a client that connects without SECURITY_SQOS_PRESENT | SECURITY_IDENTIFICATION, can be impersonated by a malicious server.

## windows-crypto — Windows cryptography API misuse

Deprecated CryptoAPI with weak algorithms; a static or zero IV; RSA without OAEP; a key derived from a password without a KDF; CryptGenRandom replaced by rand. Also CryptProtectData used for data that crosses a trust boundary it does not protect.

## windows-alloc — Windows allocator misuse

Mixing allocator families (HeapAlloc freed with free, LocalAlloc freed with HeapFree, CoTaskMemAlloc freed with delete). Size arithmetic before HeapAlloc that can overflow. HEAP_ZERO_MEMORY assumed but not passed.
