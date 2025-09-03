
# Opinion Dynamics Simulator

This project models and simulates opinion dynamics in social networks using the DeGroot and Bounded Confidence models. It allows experimentation with different graph topologies, visualization of opinion changes, and inspection of weight and opinion matrices at various stages of consensus.

## Installation
1. Install Python using the `pythoninstall` file
2. Use pip3 to install numpy, scipy, matplotlib, networkx using the command 
```
pip3 install module --user
```

3. Open Terminal and navigate to the Program folder
4. Run the program
```
python3 control.py
```

## Default Setup
By default, the simulator runs the DeGroot model on a star graph with 50 nodes across 7 issues.
It will:
- Visualize opinions at the beginning and end of each issue.
- Display weight and opinion matrices at both initialization and consensus.

## Project Structure and Controls
- **control.py** – Main entry point.
    - Modify variables such as:
        - Number of agents 
        - Graph topology (line, ring, star, random, SBM, or real-world datasets)
        - Number of conversations/issues
    - Select the opinion dynamics process (DeGroot or BoundedConfidence).
        
- **mod_degroot.py** – Adjusts visualization rates for the DeGroot model.
    
- **mod_bounded_conf.py** – Allows modification of bounds and affectivity for the Bounded Confidence model.
    
- **visualize.py** – Provides multiple visualization methods (can be imported by other modules).
    
- **csv_processor.py** – Converts a network matrix (e.g., input_stanford.csv) into an adjacency matrix for simulations.

## Further reading
- [Blog post about the project](https://dulangaj.github.io/social-network-opinion-dynamics)
- Report.pdf in the GitHub repo

## Citation

If referencing this work, please cite:
**Dulanga Jayawardena**. _Modelling and Simulating Opinion Dynamics in Social Networks Using Linear and Non-linear Models._ Final Year Project Report, Chinese University of Hong Kong, 2020
