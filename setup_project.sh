#!/bin/bash
# Project setup script 

echo "Setting up project..."
mkdir -p src data output
echo "Directories created"

# Create files using "here-documents"
cat > .gitignore << 'EOF'
EOF

cat > data/student.csv << 'EOF'
EOF

cat > src/data_analysis.py << 'EOF'
TODO
EOF

cat > src/data_analysis_functions.py << 'EOF'
TODO
EOF

chmod +x setup_project.sh