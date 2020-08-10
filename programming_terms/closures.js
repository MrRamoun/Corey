function html_tag(tag) {
	function html_content(content) {
		console.log("<" + tag + ">" + content + "</" + tag + ">")
	}
	return html_content
}

h1_tag = html_tag("h1")
html_content("hello from h1")

