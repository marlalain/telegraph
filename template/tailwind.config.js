module.exports = {
	sourceCSS: "./src/styles.css",
	outputCSS: "./css/styles.css",
	purge: {
		enabled: true,
		content: ["./*.html"],
	},
	darkMode: "media", // or 'media' or 'class'
	theme: {
		extend: {
			colors: {
				primary: {
					100: "#F1F1F1",
					200: "#9D9EA0",
					300: "#C0A097",
					400: "#9B836A",
					800: "#8A644D",
					900: "#1F1D1D",
				},
			},
		},
	},
	variants: {
		extend: {},
	},
	plugins: [],
};
