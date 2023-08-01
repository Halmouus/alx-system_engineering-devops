#!/bin/bash
for file in $(ls *.rb); do
    cat > $file << EOL
#!/usr/bin/env ruby
puts ARGV[0].scan(//).join
EOL
done