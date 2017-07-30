{
	"name": "Book Self",
	"version": "1.0",
	"author": "Shahjalal",
	"website": "",
	"category": "Tools",
	"depends": ["base"],
	"description": "Book Self Module",
	# always loaded
    "data": [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/book.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
	"installable": True
}