# lb2-2021-project-asole
LB2 project repository of Giovanni Asole

###### NOTE ######

for a full explanation of the work, check the word file "Lab2-project-Giovanni-Asole"

######## MAIN #######

The only way to fully understand many characteristics of proteins in-cluding function, interactions, localization, 
is to know their tertiary structure. Unfortunately, obtaining the tertiary structure of a protein is not an easy task,
nowadays experimental methods are widely used, among them the "standard method" is X-ray
crystallography (Bond, 2014), in comparison to other methods including Nuclear Magnetic Resonance (NMR) and Cryo-electron microscopy. 
The use of these experimental methods, however, cannot be compared with the more than exponential growth of datasets seeking to
provide high-quality information on protein function, such as UniProt. For this reason, one of the most important tasks of 
Bioinformatics is the prediction of the tertiary structure of a protein starting from its primary structure, to do this it
is necessary to have effective and very precise methods that allow to obtain the secondary structure starting from the primary sequence.

Protein secondary structure prediction began in 1951 when Pauling and Corey predicted helical and sheet conformations for
protein polypeptide backbone even before the first protein structure was determined. Secondary structure prediction 
techniques have been classified into three generations [1].
In the first generation, secondary structures were predicted from a protein sequence according to statistical propensities
of aminoacid residues towards a specific secondary structure element, The most representative method of first-generation 
methods is the Chou–Fasman method [2]. The second-generation methods, represented 
by the Garnier-Osguthorpe-Robson (GOR) method [3] and the Lim method [4], used a sliding window of neighbouring residues 
and various theoretical algorithms such as statistical information, as well as other methods that use a learning method 
including neural net-works [5]. The information obtained from the neighboring residuals allowed to increase the
precision of the prediction up to 60%.
The third generation of techniques is characterized by using evolutionary information derived from alignment of
multiple homologous sequences [6]. During this period, new computational algorithms have been implemented. Examples are 
support vector machines [7], hidden Markov network [8], PSIPRED [9].
With the third generation the accuracy on the prediction of the secondary structure reaches 70-75%.

The work described in this publication is based on the use of two main methods for the prediction of the protein 
secondary structure: GOR and SVM. The dataset used to train the two methods is jPRED4 dataset composed of 1348 
protein and a test set (blind-set) composed of 150 proteins.
For both methods, a cross-validation phase was performed first to fix the hyper parameters, followed by a train
phase on the entire dataset to produce models. Finally, the two models obtained by the two different methods 
were tested on blind-tests obtaining a prediction of the structure, which was compared with that one produced 
using the DSSP program (reduced to the three main structures), in order to re-trieve indices that allow us to compare 
the precision of the secondary structure prediction of the two methods.
This procedure finally showing that SVM method work better than the GOR one.

######## REFERENCES ########

1.	Rost B. Review: protein secondary structure prediction con-tinues to rise. J Struct Biol. 2001 May-Jun;134(2-3):204-18. doi: 10.1006/jsbi.2001.4336. PMID: 11551180.
2.	Chou PY, Fasman GD. Prediction of protein conformation. Biochemistry. 1974 Jan 15;13(2):222-45. doi: 10.1021/bi00699a002. PMID: 4358940.
3.	Garnier J, Osguthorpe DJ, Robson B. Analysis of the accuracy and implications of simple methods for predicting the secondary structure of globular proteins. J Mol Biol. 1978 Mar 25;120(1):97-120. doi: 10.1016/0022-2836(78)90297-8. PMID: 642007.
4.	Lim VI. Algorithms for prediction of alpha-helical and beta-structural regions in globular proteins. J Mol Biol. 1974 Oct 5;88(4):873-94. doi: 10.1016/0022-2836(74)90405-7. PMID: 4427384.
5.	Muggleton S, King RD, Sternberg MJ. Protein secondary structure prediction using logic-based machine learning. Protein Eng. 1992 Oct;5(7):647-57. doi: 10.1093/protein/5.7.647. Erratum in: Protein Eng 1993 Jul;6(5):549. PMID: 1480619.
6.	Zvelebil MJ, Barton GJ, Taylor WR, Sternberg MJ. Prediction of protein secondary structure and active sites using the alignment of homologous sequences. J Mol Biol. 1987 Jun 20;195(4):957-61. doi: 10.1016/0022-2836(87)90501-8. PMID: 3656439.
7.	Hua S, Sun Z. A novel method of protein secondary structure prediction with high segment overlap measure: support vector machine approach. J Mol Biol. 2001 Apr 27;308(2):397-407. doi: 10.1006/jmbi.2001.4580. PMID: 11327775.
8.	Aydin Z, Altunbasak Y, Borodovsky M. Protein secondary structure prediction for a single-sequence using hidden semi-Markov models. BMC Bioinformatics. 2006 Mar 30;7:178. doi: 10.1186/1471-2105-7-178. PMID: 16571137; PMCID: PMC1479840.
9.	D. T. Jones. Protein secondary structure prediction based on position-specific scoring matrices. Journal of Molecular Biology, 292(2):195–202, September 1999. doi:10.1006/jmbi.1999.3091. 

