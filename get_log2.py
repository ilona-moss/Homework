with open('access-log') as wwwlog:
	bytecolumn = (line.rsplit(maxsplit = 1)[1] for line in wwwlog)
	bytes_sent = (int(x) for x in bytecolumn if x.isdigit())
	print(sum(bytes_sent))
