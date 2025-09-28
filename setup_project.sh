#!/bin/bash
# Project setup script 

echo "Setting up project..."
mkdir -p src data output
echo "Directories created"

# Create files using "here-documents"
# Set up .gitignore
echo "Setting up .gitignore"
cat > .gitignore << 'EOF'
EOF

# Set up student csv with data
echo "Setting up student.csv"
cat > data/students.csv << 'EOF'
name,age,grade,subject
Alice,21,80,Math
Bob,25,95,Math
Charlie,27,92,History
Daisy,23,85,History
Ethan,24,80,Math
Fiona,22,90,Physics
Greg,20,83,Physics
EOF

# Set up two python scripts
echo "Setting up data_analysis.py"
cat > src/data_analysis.py << 'EOF'
#TODO
EOF

echo "Setting up data_analysis_functions.py"
cat > src/data_analysis_functions.py << 'EOF'
#TODO
EOF

chmod +x setup_project.sh

echo "Setup complete!"