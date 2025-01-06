file_name = 'index.html'
title_text= "쿠팡 스크래핑"
main_text = '<p>쿠팡 스크래핑한 결과가 들어간다.</p>'
html_text =f"""<!DOCTYPE HTML>
<html>
	<head>
		<title>{title_text}</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
		<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
	</head>
	<body class="is-preload">

		<!-- Wrapper -->
			<div id="wrapper">
				<!-- Header -->
					<header id="header">
						<a href="index.html" class="logo">Massively</a>
					</header>
				<!-- Main -->
					<div id="main">
						<!-- Post -->
							<section class="post">
								<header class="major">
									<span class="date">April 25, 2017</span>
									<h1>{title_text}</h1>
								</header>
								<div class="image main"><img src="images/pic01.jpg" alt="" /></div>
                                {main_text}
							</section>
					</div>
			</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.scrollex.min.js"></script>
			<script src="assets/js/jquery.scrolly.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>"""


with open(f'{file_name}', 'w', encoding='utf-8') as f:
    f.write(html_text)