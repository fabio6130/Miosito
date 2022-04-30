.PHONY: webpack

webpack:
	cd static && npx webpack --config webpack.config.js --watch
	
