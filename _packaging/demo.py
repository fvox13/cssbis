#!/usr/bin/python
import os

ICON_CLASSES = [
	{'base_class': 'action', 'display': 'Actions (<code>.action</code>)', 'file': 'actions.css',},
	{'base_class': 'browser', 'display': 'Browsers (<code>.browser</code>)', 'file': 'browsers.css',},
	{'base_class': 'country', 'display': 'Countries (ISO 3166-1 Alpha 2, plus MaxMind extensions) (<code>.country</code>)', 'file': 'countries.css',},
	{'base_class': 'filetype', 'display': 'File Types (<code>.filetype</code>)', 'file': 'filetypes.css',},
	{'base_class': 'os', 'display': 'Operating Systems (<code>.os</code>)', 'file': 'os.css',},
	{'base_class': 'programming_language', 'display': 'Programing Languages (<code>.programming_language</code>)', 'file': 'programming_languages.css'},
	{'base_class': 'severity_level', 'display': 'Severity Levels (<code>.severity_level</code>)', 'file': 'severity_levels.css'},
	{'base_class': 'socmed small16', 'display': 'Social Media (16x16) (<code>.socmed .small16</code>)', 'file': 'socmed.css',},
	{'base_class': 'socmed medium24', 'display': 'Social Media (24x24) (<code>.socmed .medium24</code>)', 'file': 'socmed.css',},
	{'base_class': 'status', 'display': 'Status (<code>.status</code>)', 'file': 'status.css',},
]

def get_classes(idict):
	parent = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
	filepath = os.path.join(parent, idict['file'])
	with open(filepath, 'r') as cssfile:
		for l in cssfile.readlines():
			if 'socmed' in idict['base_class']:
				bclass = ".".join(idict['base_class'].split())
			else:
				bclass = idict['base_class']
			if l.startswith('.%s.' % bclass) and 'withtext' not in l and 'button' not in l:
				yield l.split('.%s.' % bclass)[1].replace('{', '').replace(',', '').strip()

def print_iconclass_row(base_class, c):
	print """
				<tr>
					<td><code>.%(class)s</code></td>
					<td style="width: 110px; text-align:center">
						<a class="%(base_class)s %(class)s" href="#"></a>
						<span class="%(base_class)s %(class)s"></span>
						<input type="submit" class="%(base_class)s %(class)s" value="%(display)s" />
						<button class="%(base_class)s %(class)s">%(display)s</button>
					</td>
					<td>
						<a class="%(base_class)s withtext %(class)s" href="#">%(display)s</a>
						<span class="%(base_class)s withtext %(class)s">%(display)s</span>
						<input type="submit" class="%(base_class)s withtext %(class)s" value="%(display)s" />
						<button class="%(base_class)s withtext %(class)s">%(display)s</button>
					</td>
					<td>
						<a class="%(base_class)s button %(class)s" href="#">%(display)s</a>
						<span class="%(base_class)s button %(class)s">%(display)s</span>
						<input type="submit" class="%(base_class)s button %(class)s" value="%(display)s" />
						<button class="%(base_class)s button %(class)s">%(display)s</button>
					</td>
				</tr>
""" % {'base_class': base_class, 'class': c, 'display': c.title()}



print """
<!DOCTYPE HTML>
<html>
	<head>
		<title>CSSbis Demo Page</title>
		<link rel="stylesheet" type="text/css" href="../general.css" />
		<link rel="stylesheet" type="text/css" href="../vcr.css" />
		<link rel="stylesheet" type="text/css" href="../icons.css" />
		<link rel="stylesheet" type="text/css" href="../actions.css" />
		<link rel="stylesheet" type="text/css" href="../browsers.css" />
		<link rel="stylesheet" type="text/css" href="../countries.css" />
		<link rel="stylesheet" type="text/css" href="../filetypes.css" />
		<link rel="stylesheet" type="text/css" href="../os.css" />
		<link rel="stylesheet" type="text/css" href="../programming_languages.css" />
		<link rel="stylesheet" type="text/css" href="../severity_levels.css" />
		<link rel="stylesheet" type="text/css" href="../socmed.css" />
		<link rel="stylesheet" type="text/css" href="../status.css" />
	</head>
	<body>
		<h1>CSSbis Demo Page</h1>
		<p>This page illustrates every style present in CSSbis.</p>

		<h2>General Styles</h2>

		<h3>User Messages (<code>.usermessages</code>, <code>#usermessages</code>)</h3>
		<p>Use Django?  These go great with <code>django.contrib.messages</code></p>
		<ul class="usermessages">
			<li class="info">This is an informational message. It has the class of .info</li>
			<li class="success">This is a success message. It has the class of .success</li>
			<li class="error">This is an error message. It has the class of .error</li>
		</ul>

		<h3>Discreet Text (<code>.discreet</code>)</h3>
		<p class="discreet">Inspired by a style found in <a href="http://www.plone.org/">Plone</a>, use <code>.discreet</code> on anything you want to be... discreet!</p>

		<h3>Breadcrumbs (<code>.breadcrumbs</code>, <code>#breadcrumbs</code>)</h3>
		<p>Start with a list, end up with some basic, semantic breadcrumbs!</p>
		<ul class="breadcrumbs">
			<li><a href="#">Home</a></li>
			<li><a href="#">Main Section</a></li>
			<li>Current Page</li>
		</ul>

		<h3>Warning Box (<code>div.warning</code>)</h3>
		<div class="warning">
			<h2>Critical Warning!</h2>
			<p>Pay no attention to the man behind the curtain!</p>
			<p>If you only had a brain, you could while away the hours, conferring with the flowers, consulting with the rain.</p>
		</div>

		<h3>VCR Controls (<code>div.vcr</code>)</h3>
		<p>Use <code>span</code> tags for disabled, <code>a</code> tags for enabled. Available in <code>.dark</code> and <code>.light</code> variants.</p>
		<div class="vcr dark">
			<span class="start">Start</span>
			<span class="prev">Previous></span>
			<span class="current">Page 1 of 15</span>
			<a href="#" class="next">Next</a>
			<a href="#" class="end">End</a>
		</div>
		<br>
		<div class="vcr light">
			<a href="#" class="start">Start</a>
			<a href="#" class="prev">Previous></a>
			<span class="current">Page 15 of 15</span>
			<span class="next">Next</span>
			<span class="end">End</span>
		</div>

		<hr/>
		<h3>Basic Floated Images (<code>.floatright</code> and <code>.floatleft</code>)</h3>
		<div style="width: 800px">
			<img src="demo.jpg" alt="Demo Image" class="floatright" />
			<p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. </p>
			<p>Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna.</p>
			<img src="demo2.jpg" alt="Demo Image 2" class="floatleft" />
			<p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur?</p>
		</div>
		<hr/>

		<h3>Blockquote (<code>blockquote</code>)</h3>
		<div style="width: 800px">
			<blockquote>
				Never attempt to teach a pig to sing; it wastes your time and annoys the pig.
				<span class="attribution">&mdash; Robert Heinlein</span>
			</blockquote>
			<p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. </p>
			<p>Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna.</p>
		</div>

		<hr />

		<h2>Icon Classes</h2>
		<p>Each of the items in this section can be used separately, in which case you'll only get the icon itself, or with the "withtext" or "button" modifiers. Examples of each will follow. You can apply these classes to anchor tags, span tags, input tags (like submit buttons), and button tags, and the examples will be in that order.</p>
		<p>Also, the table the icons are in can be used if you give your table a class of <code>.cssbis</code></p>
		<ul>
"""
for icon_class in ICON_CLASSES:
	print '<li><a href="#icons_%(icon_class)s">%(display)s</a></li>' % {'icon_class': icon_class['base_class'], 'display': icon_class['display'],}
print "</ul>"


for icon_class in ICON_CLASSES:
	print """
		<h3 id="icons_%(base_class)s">%(display)s</h3>
		<table class="cssbis">
			<thead>
				<tr>
					<th>Class</th>
					<th>Icon Only</th>
					<th>Icon With Text</th>
					<th>Button</th>
				</tr>
			<tbody>
	""" % {'base_class': icon_class['base_class'], 'display': icon_class['display']}
	for c in get_classes(icon_class):
		print_iconclass_row(icon_class['base_class'], c)
	print """
			</tbody>
		</table>
	"""

print """
	</body>
</html>
"""
