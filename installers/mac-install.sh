cd $HOME
conda create -y -n qis101 python=3.9
conda activate qis101
conda config --env --add channels conda-forge
conda config --env --set channel_priority strict
conda install -y mayavi
conda install -y numpy
conda install -y numba
conda install -y matplotlib
conda install -y sympy
conda install -y scipy
conda install -y scikit-learn
conda install -y pulp
conda install -y pandas
conda install -y pandasql
conda install -y docutils
conda install -y pandocfilters
conda install -y numexpr
conda install -y h5py
conda install -y traitsui
conda install -y pathspec
conda install -y openpyxl
conda install -y pylint
conda install -y autopep8
conda install -y black
conda install -y websockets
conda install -y requests
conda install -y pyserial
conda install -y nodejs
conda install -y jupyterlab
conda install -y jupyterlab_widgets
conda install -y jupyterlab_code_formatter
conda install -y ipympl
pip install pygame
pip install 'qiskit[all]'
code --install-extension ms-vscode.cpptools
code --install-extension ms-vscode.cpptools-extension-pack
code --install-extension ms-vscode.powershell
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-toolsai.jupyter
code --install-extension visualstudioexptteam.vscodeintellicode
code --install-extension streetsidesoftware.code-spell-checker
code --install-extension ms-vscode.cmake-tools
code --install-extension davidanson.vscode-markdownlint
code --install-extension esbenp.prettier-vscode
code --install-extension mechatroner.rainbow-csv
code --install-extension emmanuelbeziat.vscode-great-icons
code --install-extension james-yu.latex-workshop
code --install-extension cschlosser.doxdocgen
code --install-extension redhat.vscode-yaml
code --install-extension eamodio.gitlens
echo 'y' | jupyter lab --generate-config
echo 'c.ServerApp.use_redirect_file = False' >> $HOME/.jupyter/jupyter_lab_config.py

