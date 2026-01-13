tailwind.config = {
    darkMode: 'class',
    theme: {
        extend: {
            colors: {
                cyber: {
                    black: '#050505',
                    dark: '#0f0f0f',
                    surface: '#18181b', // Zinc 900
                    cyan: '#00F0FF',    // Electric Blue (CP77)
                    pink: '#FF003C',    // Radical Red (CP77 Glitch)
                    blue: '#007bff',    // Professional Blue
                    purple: '#7000FF',  // Deep Neon Purple
                    dim: 'rgba(0, 123, 255, 0.1)',
                    slate: '#2d2d2d'
                }
            },
            fontFamily: {
                sans: ['Rajdhani', 'sans-serif'],
                display: ['Orbitron', 'sans-serif'],
                mono: ['Share Tech Mono', 'monospace'],
            },
            backgroundImage: {
                'cyber-grid': "linear-gradient(to right, rgba(0, 123, 255, 0.05) 1px, transparent 1px), linear-gradient(to bottom, rgba(0, 123, 255, 0.05) 1px, transparent 1px)",
                'cyber-noise': "url('data:image/svg+xml,%3Csvg viewBox=%220 0 200 200%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22noiseFilter%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%220.65%22 numOctaves=%223%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23noiseFilter)%22 opacity=%220.05%22/%3E%3C/svg%3E')",
                'gradient-glow': 'radial-gradient(circle at center, rgba(0, 240, 255, 0.15) 0%, transparent 70%)',
            },
            boxShadow: {
                'neon-cyan': '0 0 5px rgba(0, 240, 255, 0.5), 0 0 10px rgba(0, 240, 255, 0.3)',
                'neon-red': '0 0 5px rgba(255, 0, 60, 0.5), 0 0 10px rgba(255, 0, 60, 0.3)',
                'neon-blue': '0 0 5px rgba(0, 123, 255, 0.5), 0 0 10px rgba(0, 123, 255, 0.3)',
            },
            animation: {
                'pulse-fast': 'pulse 1s cubic-bezier(0.4, 0, 0.6, 1) infinite',
                'glitch-skew': 'glitch-skew 1s cubic-bezier(0.25, 0.46, 0.45, 0.94) both infinite',
            },
            keyframes: {
                'glitch-skew': {
                    '0%': { transform: 'translate(0)' },
                    '20%': { transform: 'translate(-2px, 2px)' },
                    '40%': { transform: 'translate(-2px, -2px)' },
                    '60%': { transform: 'translate(2px, 2px)' },
                    '80%': { transform: 'translate(2px, -2px)' },
                    '100%': { transform: 'translate(0)' }
                }
            }
        }
    }
}
