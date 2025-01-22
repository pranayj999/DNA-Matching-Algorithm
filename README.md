# DNA-Matching-Algorithm

# Introduction 
The idea of genome mappability, originally proposed by Derrien [1], is an analytical  method that aims to assess the intricacy and recurrence of the genome. The metric  particularly quantifies the ability to uniquely identify sequences within the genome,  considering substrings of a predetermined length, denoted as m, and allowing for a  specific amount of variants or mismatches, indicated as k. The measure holds  significant importance in the field of genomics as it serves to quantify the recurring  pattern across the genome. It counts the frequency at which a certain substring,  originating from a specific genomic location, is reproduced elsewhere throughout the  genome, resulting in a maximum of k mismatches.  
In order to determine genome mappability, scientists conduct an analysis of every  place within the genome, monitoring the frequency of its corresponding substring  over the whole genomic sequence while adhering to specific limits for length and  tolerance for mismatches[3]. The assessment of this metric is crucial in  comprehending genomic regions characterized by either distinct sequences,  facilitating their identification, or excessive repetition, which can pose challenges in genetic research and interpretation. A comprehensive comprehension of mappability  is necessary for a wide array of activities, encompassing genome assembly, the  development of probes and primers in experimental techniques, and the precise  interpretation and mapping of sequencing data[2]. Therefore, the capacity to map the  genome not only uncovers the intricate structural characteristics of the genome but  also has a significant impact on the approaches and technology employed in genomic  research.

# Background and Case Study 
The quantification of the repeat structure of a genome is a crucial statistic known as  genome mappability, which evaluates the degree of uniqueness in mapping genomic  sequences. The aforementioned idea has significant importance in the identification  of genomic areas that can be sequenced and aligned with precision, hence enabling  dependable genetic analysis. The concept of mappability has significant importance  in the context of precise genome assembly and efficient variant discovery, as it aids  in differentiating between distinct sequences and redundant ones present within the  genome[6]. Through the assessment of the mappability of a genome, scientists may  gain a deeper comprehension of the genomic terrain, including the arrangement and  occurrence of repetitive sequences, which frequently provide difficulties in  sequencing endeavors[5]. Regions with high mappability are characterized by the  presence of distinct sequences that are favorable for accurate mapping. Conversely,  regions with poor mappability are indicative of areas that may have misalignment as  a result of repeated sequences. In conclusion, this metric improves the accuracy and  reliability of interpreting genomic data, hence promoting progress in genetic research  and customized therapy.
• Suffix of a Sequence: For a given sequence S[1,n],Si represents the suffix  starting at position i, defined as S[i,n]. 
• Longest Common Prefix (LCP): The function LCP(P,Q) denotes the longest  common prefix between two strings P and Q. 
• Lcp Function: Given two indices i and j, lcp (i,j) denotes the length of LCP  (Si,Sj), i.e., |LCP(Si, Sj)|. 

A suffix tree, represented as ST, is a compact trie that represents all suffixes of a  string S[1,n]. It concludes with a terminal symbol '$' that is the shortest  lexicographically consistent, ensuring that each leaf represents a distinct suffix. 

• Node Definitions: 
• r: Root of the tree. 
• u,v: Arbitary nodes within the tree, where u is not equal to r. 
• Parent and Ancestor Relations: parent(u) is the parent node of u. A node u  is considered an ancestor of v if it lies on the path from the root r to v.
• Lowest Common Ancestor(LCA): LCA(u,v) identifies the lowest common  ancestor of nodes u and v. 
• Path and String Depth: path(u) concatenates lables from the root to u. The  string depth strDepth(u) is the length of this path. 
• Subtree Characteristics: The subtree rooted at u is identified, and the size  size (u). represents the count of leaves in this subtree. Strings(u) denotes the  set f substrings derived from the leaves of the subtree rooted at u. 

The construction of suffix trees for an integer alphabet is achieved in O(n) time and  space, owing to the utilization of optimized algorithms that take into consideration  the characteristics of the tree structure [1]. The computation of the Life Cycle  Assessment (LCA) for any two nodes in the suffix tree may be accomplished in  constant time, enabling the computation of the Life Cycle Probability (LCP) for any  two suffixes in a similar manner within constant time. 

Numerous strategies have been developed in research to tackle the computational  difficulties linked to genome mappability.
• Heuristic Solutions: Derrien et al. (2012) [1] introduced heuristic algorithms  to approximate mappability for substrings of length m with tolerance for k  mismataches. 
• Algorithms by Alzamel el al.(2017)[1]: 
1. An O(n log n log log n) time complexity algorithm. 
2. An O(nm) time complexity algorithm. 
3. An O(n) average-case time algorithm when m = Omega(log n).

# Methodology 
• Our Algorithm 
In the Initial stages of the algorithm, we construct a compact trie T, specifically  designed to contain all substrings of length m extracted from the sequence S. This  trie is meticulously assembles such that each leaf, denoted as l, encapsulates a  comprehensive list of the starting indices within S that correspond to the substring  mapped by the path from the root to l. This structure allows for an organized  representation of substring locations across S, facilitating efficient access and  manipulation in late stages of the algorithm. 

Following the trie construction, the algorithm proceeds with a heavy path  decomposition of T. This sophisticated technique segments the trie into various paths,  distinguishing each based on the ‘heaviness’ – a measure typically defined by the  number of descendant leaves a node possesses. Nodes with a larger descendant count  lead to ‘heavier’ paths. This decomposition is strategic it optimizes the trie’s structure by minimizing the depth of frequently accessed elements, thus reducing the  complexity of and enhancing the speed of traversal operations. 

After decomposing the trie into heavy paths, the subsequent phase involves the  meticulous processing of each individual path. This step is crucial and involves the  deployment of two specialized types of auxiliary trees for every path within the trie.  These auxiliary trees are integral to the algorithm’s functionality, serving dual  proposes: first, to streamline the traversal process across the compact trie and second,  to efficiently manage and compare the myriad of substrings contained within. 

The primary functions of these auxiliary trees is to facilitate a rapid and accurate  comparison of substrings S[j,j+m-1] for each index j that differs from i, ensuring that  each comparison allows for at most one mismatch. This capability is essential for  applications such as genomic sequencing, where even a single nucleotide difference  can critically alter the interpretation of results. The trees enable them to swiftly navigate through the possible substring matches and mismatches, applying efficient algorithms to detect and record these occurrences.

The traversal of these auxiliary trees is methodically structured to exhaustively  explore all potential matches. This exhaustive approach ensures that no possible  substring match is overlooked, which is vital for ensuring the comprehensive analysis required in fields like bioinformatics. By Integrating heavy path decomposition with  the strategic use of auxiliary trees, the algorithm not only maximizes efficiency but  also enhances the accuracy of the matching process, making it a robust tool for  complex pattern matching scenarios often encountered in scientific research and data  analysis. 

• Constructing the Compact Trie T: 
Following the efficient construction of the suffix tree ST for sequence S in terms of  both time and space, the subsequent step involves the pruning of any branches inside  ST that exclusively consist of leaves with a string depth below m. Following this, in the case of any branch inside the set ST that surpasses a string depth of m, we  terminate the branch at this depth and introduce a new leaf node at the truncation point. The aforementioned procedure yields a recently constructed compact trie,  denoted as T. In the given compact trie T, it is possible to easily compute the set of  initial indices that correspond to the substring represented by ℎ(ℑ) path(℡), which  has a length of m and begins from S, for each leaf node ℓ ℓ. Although it is not  necessary to arrange these lists of indices in a certain sequence, the leaves themselves  possess a lexicographical arrangement that is determined by the substrings they  represent, similar to their arrangement in a suffix tree[8]. This particular arrangement  guarantees that although the trie is condensed, it maintains crucial ordering  characteristics that enable effective retrieval and processing of data. 
• Heavy Path Decomposition 
<img width="581" alt="Screenshot 2025-01-21 at 10 09 13 PM" src="https://github.com/user-attachments/assets/0708f227-c692-4dd6-a0b5-82ff74678027" />

<img width="581" alt="Screenshot 2025-01-21 at 10 09 38 PM" src="https://github.com/user-attachments/assets/fee32b37-1ed6-4acf-b981-b377fb638ba4" />

1) Identifying Heavy Paths 
The tree is examined from the root to determine the 'heavy' path, which refers to  the path from a node to its child with the highest number of descendants. The size  of the subtrees rooted at each child is typically the determining factor.  The emphasized pathways in the figures, perhaps shown in various hues, are most  likely indicative of the heavy paths. For example, it is possible that a path with a  magenta hue was employed to indicate the first heavy path originating from the  root. 

2) Decomposing the Trees
After the identification of the heavy path, it is then demarcated or isolated from the  remaining portions of the tree. The heavy path will consist of a continuous series of  nodes that extend from the uppermost point of the tree in a downward direction.  As the algorithm iterates over the tree, it may highlight other heavy pathways in  successive figures 1 & 2 using other colors, indicating their origin from distinct  subtrees. 

3) Truncating Non Heavy Paths 
Light edges, which are branches that are not part of the heavy path, diverge from the  heavy path. The shorter length of the heavy path is attributed to the fact that it is  determined by the longest path of nodes with the highest number of descendants.  Within the series of visual representations, one may observe branches that lack  emphasis, indicating their exclusion from the primary dense trajectory and  subsequent truncation for the purpose of decomposition. 

4) Utilizing the Decomposition 
Following the process of decomposition, algorithms are able to enhance their  efficiency in processing heavy pathways, since these paths are anticipated to be the  ones visited with the most frequency. The heavy-light decomposition can be utilized  to optimize operations such as LCA (Lowest Common Ancestor) inquiries or path queries.  
The figures 1 & 2 depict the progression of the tree as it undergoes decomposition, resulting in the final images that highlight the tree's distinct heavy paths and light  edges. These images are now prepared for fast traversal and query processing. 

• S Tree Construction 
The rapid merging procedures described in reference [20] are utilized to merge the  sorted lists of shortened changed suffixes associated with each branch off the  heavy path at a specific node. The sorting of these items has been confirmed by  Observation 2. The comparison between the strings may be performed in constant  time according to Lemma 4. In order to do this, it is necessary for each element  inside these lists to retain the following information: a reference to the leaf in T,  as well as the respective position and character substitution that has been  applied.  
Upon completion of the sorting process, all index lists are designated as changed  lists. If two adjacent entries in the sorted list of truncated modified suffixes are  determined to have the same length (lcp) as m, then their modified index lists are  merged. Following the completion of the 305 step, the s-Tree may be derived by  utilizing the lcp values between the updated suffixes, in a manner akin to the  process of obtaining the suffix tree from a suffix array and lcp array. The process  involves iterating over the sorted lists of truncated modified suffixes, arranging  them in ascending order, while also preserving a reference to the leaf of the  truncated modified suffix that was placed before. Once a new element is  encountered in the sorted 310 list, the process involves traversing upwards from the leaf node in order to identify the insertion location for the subsequent element  to be inserted.

#Implementation 
• Applying the 1-mappability algorithm on a toy example 
<img width="581" alt="Screenshot 2025-01-21 at 10 11 53 PM" src="https://github.com/user-attachments/assets/e4c3718c-4dc5-4683-b4f7-f6ee693df9c9" />

The Figure 3 presented here demonstrates the process of segmenting a trie, which  represents a sequence 'S', using heavy path decomposition. At the outset, we  commence with the whole trie, which then divides into all conceivable substrings of  'S'. In order to enhance the efficiency of this intricate framework, we employ the  heavy path decomposition methodology. 

The user possesses a string S, marked as "CCACAAACA," which has a length  designated as n. The user is interested in obtaining substrings of length m, namely in  this case, m=3. 

A suffix tree is generated for the string S. The provided trie is a condensed  representation that encompasses all potential suffixes of the string S. To distinguish  the heavy pathways from the other paths in the tree, it may be necessary to highlight or identify them using a color or a line. In your description, you have identified nodes  1, 2, 3, U 1, U 2, U 3, and U 4, which may represent nodes on the heavy path. For  any node U (such as 1 , 2 , 3 , U 1,U 2,U 3, and 4 U 4), a sub-tree () S−Tree(U) may  be built. The sub-tree in question encompasses the node U and its subsequent  descendants inside the suffix tree ST. The function effectively represents the segment 
of the string S that is denoted by the path from the root of ST to U, and thereafter to  all the leaves derived from U. 

The numerical values adjacent to the leaves in the S trees may indicate the initial  index of each suffix in the original string S, which corresponds to the path from the  root to that particular leaf. These indices aid in the identification of the particular  suffixes included in the string S. In practical algorithms, after identifying the heavy  paths and constructing S-Trees for the key nodes, these structures can be utilized to  conduct efficient searches and queries. For example, they can be used to find the  longest common substrings or identify repeat patterns and mappability in genome  sequencing.

<img width="581" alt="Screenshot 2025-01-21 at 10 12 56 PM" src="https://github.com/user-attachments/assets/fc9b2594-fa7f-46c9-8605-4545b0389703" />

The first step entails constructing a trie using the provided string S. Following this,  the trie structure determines the 'heavy pathways'. The phrase 'heavy path' refers to a  path that originates from a specific node and descends to a terminal node, whereby  the child node with the greatest number of descendants is chosen at each junction.  The objective of discovering these heavy pathways is to focus on the paths that align  with the substrings that occur most frequently or have the greatest length in the  dataset S. By employing a systematic approach, the trie may be optimized by  prioritizing the most important pathways, which are often the ones that contain the  most information or are most pertinent to the future calculations. 

The nodes 1, 2, U 1, U 2, and so on, symbolize pivotal points in the trie that serve as  the origins for heavy pathways. The significance of these nodes lies in their role as  the beginning points for the pathways with the highest 'weight', indicating the amount  of data positioned underneath them in the trie. An hp-tree is produced for each  significant node, denoted as U1 and U2. The hp-tree encompasses the node and its  descendent nodes that are integral components of the heavy path. It is simply a  portion of the bigger trie that specifically focuses on the most important substrings. The terminal nodes of each hp-tree correspond to separate substrings that have been  retrieved from the string S. The nodes are labeled with integer values that probably  indicate the starting points inside the string S from which the substrings, as  determined by the path leading to each leaf, come from.  

Furthermore, the process of constructing hp-trees, also known as heavy path trees, is  a methodical approach to representing and structuring substrings derived from a  larger sequence. In this approach, each leaf serves as a reference to the specific  location within the original string where these substrings may be located. The  inclusion of number annotations is of utmost importance as they serve as a direct  point of reference to the precise position inside the original string T. This mapping  successfully associates each substring with its own initial position. The establishment  of this mapping facilitates a direct connection between the hp-tree structure and the  sequence S, hence enabling quick retrieval and analysis of the substrings.  

The annotations function as both a basic index and a tool for comprehending the  sequential arrangement of S. These tools provide the rapid identification of the  relative location of each substring inside the bigger text. Moreover, substrings play a  pivotal part in applications where the position inside the original string has  importance, such as in genomic sequence analysis, pattern matching, or any computer  procedure where the arrangement and placement of substrings are crucial for the  analysis or outcomes. The utilization of a systematic and annotated methodology  offers a robust instrument for effectively exploring and decoding intricate string  sequences.

By strategically organizing the trie into hp-trees, the method effectively focuses on  the most computationally intensive paths in the structure. The implementation of this  strategic restructuring of the data structure facilitates the improvement of several  activities, including pattern identification and the computation of metrics connected  to strings. This is achieved by enhancing the navigability of the pathways that hold  the highest relevance, characterized by their substantial weights. On the other hand,  the substrings that occur less often and do not align with these primary trajectories  can be handled separately as required.  

Expanding upon this notion, the technique of dividing the trie into hp-trees enables a  more intricate approach to the administration of data. When doing a search or  calculation, the method has the ability to exploit the dense pathways in order to  decrease the search space and enhance efficiency. The aforementioned pathways,  which serve as the central points for recurring or significant substrings, offer an  efficient pathway for the algorithm to traverse, resulting in expedited and more  precise outcomes.  

The distinction between the high-priority thick pathways and the lower-priority thin  paths enables the implementation of a hierarchical processing approach. Operational  duties of more importance are assigned to the dense portions of the trie where the  substrings of greater significance are situated, while less important jobs are assigned  to the sparser regions. As a result, this can lead to a substantial decrease in the total  computing burden and utilization of resources.  

Furthermore, the method has the capability to apply customized routines that are  specifically designed to manage the lower frequency or relevance of substrings by  separating them from the heavy path. The act of separating these substrings  guarantees that they do not excessively utilize computing resources, therefore  enhancing the efficiency of the system.  

From a computational perspective, the implementation of a restructured trie has the  potential to significantly decrease the time complexity of diverse algorithms, particularly when dealing with extensive datasets like those found in genetic  sequencing. The use of heavy path decomposition enhances the proficiency of  algorithms in managing intricate inquiries, resulting in more sophisticated and  concentrated computing procedures. 

<img width="581" alt="Screenshot 2025-01-21 at 10 14 38 PM" src="https://github.com/user-attachments/assets/3e532c25-5c97-4500-9246-95580cf32b03" />

The given string S is accompanied by a comprehensive description of its character  sequence and total length. In close proximity, a table is shown that examines  substrings of a predetermined length, denoted as m, which is explicitly defined as 3.  The following table presents a compilation of several initial positions, represented as  i, inside string S, and identifies the related substrings that originate from these  positions. Furthermore, the Figure 5 appears to provide a quantitative representation  of the frequency or maybe the corresponding scores of these substrings, denoted as  F0[i] and F1[i]. F0[i] likely represents the number of instances that a substring  matches exactly elsewhere in string S, but F1[i] may show the frequency of matches  that can accept up to one difference or mismatch.  
Furthermore, it is worth noting that this table may play a crucial role in the field of  pattern recognition or sequence analysis since it offers a dual-level frequency evaluation. The F0[i] values provide information on the frequency of identical  substring repeats in the main sequence, which is a crucial factor in determining the  uniqueness and redundancy of the sequence. Conversely, the F1[i] values provide a  more comprehensive viewpoint by taking into consideration close matches, which is  especially relevant in situations where variances, such as genetic mutations, need to  be taken into account. This extensive evaluation facilitates a nuanced comprehension  of the structure of the sequence and the extent to which the sequence's pattern  occurrences are flexible or limited. The examination of sequence data analysis has  great significance in domains that strongly depend on it, such as genomics. In these  disciplines, the comprehension of sequence specificity and variability may  significantly impact the interpretation of genetic information and the consequent  biological inferences made. 

The Figure 5 presents data that demonstrates a frequency analysis of substrings with  a length of m inside the sequence S. The study differentiates between precise matches  (F0) and matches that include the potential for a single variance (F1). Consider, for  instance, the sequence "CCA" that begins at the initial position. It does not occur  again in S as a perfect match, resulting in an F0 value of 0. However, it is recognized  three times when a single mismatch is allowed.  

The utilization of this analytical approach has significant importance in the field of  genome sequencing, as the identification of mismatches may indicate the presence of  genetic variation or indicate the occurrence of mutations. Indicators such as F0 and  F1 provide valuable insights into the level of distinctiveness exhibited by a certain  sequence pattern in relation to a reference sequence. The notion of 'mappability' has significant importance in comprehending the precision with which sequences may be  identified and delineated in genomic investigations. The acquisition of precise  mappability data is of utmost importance for researchers in order to ascertain distinct  sections of the genome and identify those that may harbor possible alterations. This  information significantly influences the dependability of genomic analysis and the  formulation of treatment approaches. 

Furthermore, mappability information plays a crucial role in interpreting genomic  data, impacting several aspects such as identifying disease-related mutations and  comprehending evolutionary mechanisms. Scientists can assess the probability of  successful sequence mapping by calculating F0 and F1 values throughout a genetic  sequence. This is crucial in fields like diagnostic testing, where differentiating  between closely similar sequences helps decide the right diagnosis. The  aforementioned degree of analysis is a valuable contribution to the wider domain of  bioinformatics, as it provides comprehensive sequencing data that facilitates the  investigation of genetic functions, relationships, and intricate molecular dynamics  inside living organisms.

# Future Work 
The progress made in heavy path decomposition algorithms and their use in  evaluating sequence mappability presents promising opportunities for future  investigation, specifically in enhancing and expanding computational strategies to  address the requirements of growing genomic datasets. The incorporation of parallel  computing frameworks and the integration of complex machine learning models  present opportunities for improving algorithmic precision and handling capabilities.  These advancements seek to enhance the speed and efficiency of data processing  systems. The creation of analytical tools and visual interfaces that prioritize the needs  and preferences of users would serve as a means to connect elaborate computational  processes with their practical implementation in precision medicine. This would  enable the implementation of individualized treatment strategies that are informed by  a comprehensive understanding of individual genetic profiles.  

Furthermore, the advancement of mappability criteria, which have been developed to  incorporate a wider range of genetic inconsistencies, such as different mismatches  and insertion-deletion events (indels), has the potential to significantly transform the  field of comparative genomics and the examination of evolutionary trends. The  possibility exists to reveal the complex mechanisms through which genetic diversity  impacts biological functions and phenotypes by integrating mappability measures  with multiple genomic datasets and varied omic sciences. In the context of the  emerging field of computational genetics, it is crucial to adopt a conscientious stance  towards the ethical, legal, and societal implications that arise from the enhanced availability and interpretive capabilities of genetic information. To promote  responsible growth in genomic research and ensure its effective and morally sound  applications, it is crucial to navigate these challenges with a balanced approach.

# Conclusion 
To summarize, the advancements achieved in improving the ability to map the  genome using advanced heavy path decomposition methods mark the beginning of a  new age in computational genomics. The intricate characteristics of genomic  sequences necessitate robust and adaptable computational methodologies in order to  unravel their multiple patterns. The algorithmic advancements attained in this  research serve as a fundamental basis for the enhanced and intricate examination of  genomic data. Through the use of heavy path decomposition, scientists may  accurately assess the mappability of the genome, which is crucial for gaining a more  profound understanding of genetic diversity and its impact on health outcomes and  disease symptoms. This study highlights the significant importance of advanced  computational tools in advancing genetic research and stresses their essential  contribution to the development of personalized treatment approaches in the field of  precision medicine. As we contemplate the forthcoming period, it becomes evident  that continuous investigation in this field, carried out with a diligent approach to the  ethical handling of sensitive genetic data, holds the capacity to not only broaden the  range of genomic examinations but also to profoundly impact the endeavor for  tailored health interventions. The completion of this research represents not just an  academic achievement, but also a step towards a future when computational  genomics is utilized to bring about significant and practical improvements in both  societal well-being and individual health.

