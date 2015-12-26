####Singular Value Decomposition


Computing the principal components amounts to calculating the covariance matrix of the data and computing the eigenvalues and eigenvectors of the covariance matrix. This gets to be computationally expensive for large numbers of rows and columns in the data matrix. When PCA is computationally expensive, Singular Value Decomposition (SVD) can be used instead.

SVD is one of many methods to perform matrix decomposition. It breaks apart matrices into combinations of column and row vectors. The column and row vectors each form an orthogonal vector space, so there is no redundant information between pairs. SVD also finds a weight, called a singular value, associated with each combination of column and row vectors. The singular values determine how much each combination contributes to the construction of the final matrix.

Since computation of the SVD is much more computationally efficient than the basic PCA algorithm, SVD is usually used to compute PCA.


[Singular Value Decomposition Tutorial by Kirk Baker]
(https://www.ling.ohio-state.edu/~kbaker/pubs/Singular_Value_Decomposition_Tutorial.pdf)<br>
Most tutorials on complex topics are apparently written by very smart people whose goal is
to use as little space as possible and who assume that their readers already know almost as
much as the author does. This tutorial's not like that. It's more a
manifestivus for the rest of
us
. It's about the mechanics of singular value decomposition, especially as it relates to some
techniques in natural language processing. It's written by someone who knew zilch about
singular value decomposition or any of the underlying math before he started writing it,
and knows barely more than that now. Accordingly, it's a bit long on the background part,
and a bit short on the truly explanatory part, but hopefully it contains all the information
necessary for someone who's never heard of singular value decomposition before to be able
to do it
