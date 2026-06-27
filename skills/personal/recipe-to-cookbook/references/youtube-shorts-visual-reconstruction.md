# YouTube Shorts visual recipe reconstruction

Use this reference when a cooking Short has no usable description/transcript and the recipe must be reconstructed from the video itself.

## Proven workflow

1. Try normal source hierarchy first: metadata/description, transcript/subtitles, then creator site or matching social repost.
2. If transcript is unavailable, download or inspect the video locally and extract evidence frames rather than guessing from the title.
3. Create contact sheets for broad coverage:
   - 0–30 seconds: title, raw ingredients, early prep.
   - 30–60 seconds: cooking, assembly, final plating.
4. Extract individual frames around ambiguous moments at 1–2 second intervals; tighten to 0.5–1 second around fast cuts if necessary.
5. Ask vision questions as fact-finding prompts, not recipe prompts:
   - “What ingredients are visible?”
   - “What action is happening?”
   - “What text appears on screen?”
   - “Is this potato, egg, cornichon, artichoke, or another ingredient?”
6. Separate three categories in the final recipe:
   - **Visible/confirmed:** ingredients and actions clearly shown.
   - **Inferred culinary glue:** dressing ratios, seasoning, approximate times, quantities.
   - **Uncertain:** visually ambiguous ingredients or steps.
7. In the final answer, explicitly state when transcript/description were unavailable and that the recipe is reconstructed visually.

## Useful command patterns

Use a downloader such as `yt-dlp` through the available package runner if no system binary exists:

```bash
uvx --from yt-dlp yt-dlp --dump-json --skip-download '<youtube-url>'
uvx --from yt-dlp yt-dlp -f 'bv*[height<=720]+ba/b[height<=720]/best' --merge-output-format mp4 -o '/tmp/recipe_%(id)s.%(ext)s' '<youtube-url>'
```

Extract contact sheets and frames with ffmpeg:

```bash
ffmpeg -hide_banner -loglevel error -y -ss 0 -t 30 -i video.mp4 -vf "fps=1/2,scale=270:-1,tile=5x8" contact_0_30.jpg
ffmpeg -hide_banner -loglevel error -y -ss 30 -t 30 -i video.mp4 -vf "fps=1/2,scale=270:-1,tile=5x8" contact_30_60.jpg
ffmpeg -hide_banner -loglevel error -y -ss 40.5 -i video.mp4 -frames:v 1 -q:v 2 frames/frame_40_5.jpg
```

## Final-answer wording

Good disclosure line:

> Описание/субтитры недоступны, поэтому рецепт восстановлен по визуальному разбору ролика; граммовки и часть заправки — кулинарные ориентиры, не точные данные автора.

Avoid presenting guessed amounts as if the creator specified them.