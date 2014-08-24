first_bytes=scan("first_bytes.log")
first_mean = mean(first_bytes)
first_var = var(first_bytes)

download_time=scan("download_time.log")
download_mean = mean(download_time)
download_var = var(download_time)

X=cat("\n\nTime to first byte:\nmean ",first_mean, "\nvariance ",first_var,"\n\nDownload time:\nmean ",download_mean,"\nvariance ",download_var,"\n")

