
task :build do
	npm_install = ENV['npm_install']
	system('rm -rf dist')
	if npm_install.nil? 
		npm_install = 'true'
	end
	if npm_install == 'true'
		puts 'running npm...'
		system('npm install')
	end
	puts 'running gulp...'
	system('gulp')
end

task :distribute do
	dist_dir = "dist"
	index_file = "#{dist_dir}/index.html"
	master_access_key = ENV['master_access_key']
	master_secret_key = ENV['master_secret_key']
	if not File.exists? index_file
	  raise "build task must be run, missing #{index_file}"
	end
	if master_access_key.nil?
		raise 'missing master_access_key'
	end
	if master_secret_key.nil?
		raise 'missing master_secret_key'
	end
	puts "publishing swagger-ui"
	s3_location = "socotra-swagger-ui"
	path_inject = "AWS_DEFAULT_REGION=\"eu-west-1\" AWS_ACCESS_KEY_ID=\"#{master_access_key}\" AWS_SECRET_ACCESS_KEY=\"#{master_secret_key}\" "
	cmd_sync = "cd #{dist_dir} && #{path_inject} aws s3 sync . s3://#{s3_location} --acl public-read"
	puts cmd_sync
	success = system(cmd_sync)
	if not success
		raise "distribution failed on aws sync"
	end
	puts "distribution success to s3: #{s3_location}"
end
