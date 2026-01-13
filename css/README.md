# Styles Configuration

The CSS styles for this project are currently located inline within `code.html` inside a `<style type="text/tailwindcss">` block.

## Why are they inline?

This project uses the **Tailwind CSS Play CDN** for rapid development and styling. The CDN automatically scans the DOM for utility classes and processes custom styles defined in `<style type="text/tailwindcss">` blocks.

## Moving to External CSS

If you wish to move these styles to an external file (e.g., `styles.css`), the Tailwind Play CDN **will not** automatically process the `@apply` directives or Tailwind config references within that external file.

To support external CSS files with Tailwind features, you would need to set up a build process (using Node.js, PostCSS, and Tailwind CLI).

## Current Setup

- **Scripts**: Separated into `js/tailwind.config.js` and `js/main.js`.
- **Styles**: Kept inline to ensure compatibility with the CDN setup.
