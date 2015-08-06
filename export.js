$('#flights tbody tr').each(
	function(i,e) { 
		console.log(
			$(e).find('td:first')
				.text()
				.replace('\n',' ') + 

			', ' + 

			$(e).find('td:nth-child(2) > a')
				.map(
					function() { 
						return $(this).text();
					}
				)
				.toArray()
				.join(', ')
		);
	}
);