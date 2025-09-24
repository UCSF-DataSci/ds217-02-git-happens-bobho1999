#!/bin/bash
# Project setup script 

echo "Setting up project..."
mkdir -p src data output
echo "Directories created"

# Create files using "here-documents"
echo "Setting up .gitignore"
cat > .gitignore << 'EOF'
EOF

echo "Setting up student.csv"
cat > data/student.csv << 'EOF'
name,age,grade,subject
EOF

echo "Setting up data_analysis.py"
cat > src/data_analysis.py << 'EOF'
TODO
EOF

echo "Setting up data_analysis_functions.py"
cat > src/data_analysis_functions.py << 'EOF'
TODO
EOF

chmod +x setup_project.sh