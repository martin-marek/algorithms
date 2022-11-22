### ELBO
- we're looking to approximate the true posterior $p(w | D)$ with $q_\lambda(w)$ – the $\lambda$ denotes here the parameters of the posterior   
- let's say that the best approximation $q(w)$ is the one that minimizes the KL divergence $D_{KL}(q||p)$
- we can reqrite the KL divergence as follows:
$$
\begin{aligned}
D_{K L}(q_\lambda(w) || p(w | D)) &=E_{q_\lambda(w)}\left[\log \frac{q_\lambda(w)}{p(w | D)}\right] \\
&=E_{q_\lambda(w)}\left[\log \frac{q_\lambda(w) p(D)}{p(w, D)}\right] \\
&=E_{q_\lambda(w)}[\log p(D)]+E_{q_\lambda(w)}\left[\log \frac{q_\lambda(w)}{p(w, D)}\right] \\
&=\log p(D)-E_{q_\lambda(w)}\left[\log \frac{p(w, D)}{q_\lambda(w)}\right] \\
&= \log p(D) + \textrm{ELBO}
\end{aligned}
$$

Notice that $\log p(\mathcal{D})$ does not depend on ${q_\lambda(\mathbf{w})}$, so minimizing $D_{K L}\left(q_\lambda(\mathbf{w}) \right)$ is *equivalent* to maximizing the $\textrm{ELBO}$. Also, the $\textrm{ELBO}$ provides a lower bound on the evidnece, hence the name.
$$
\begin{aligned}
\textrm{ELBO} &= \log p(D) + D_{K L}(q_\lambda(w) || p(w|D)) \\
\textrm{ELBO} &\geq \log p(D) \\
\end{aligned}
$$
### EM
- the "classic" answer for how to perform maximum likelihood estimation in models with latent variables
- notation:
	- $z$ - latent variables
	- $\theta$ - parameters
	- $D$ - dataset
- algorithm
	- alternate:
		- *E step:* compute posterior over latent variables: $p(z | D, \theta)$
		- *M step:* set $\theta$ to maximize likelihood: $\theta \leftarrow \textrm{argmax} p(D|\theta) = \textrm{argmax} E_{p(z|\theta)}[\log p(D,z|\theta)]$
- *E step*
	- assume $\theta$ is fixed 
	- computing the true posterior $p(z|D,\theta)$ might be difficult
	- to simplify the calculation, we might prefer to approximate the true posterior $p(z|D,\theta)$ by a simpler distribution $q_{\lambda}(z)$ – parametrized by $\lambda$
	- recall: minimizing KL divergence is equivalent to maximizing the ELBO
	- $\textrm{ELBO} = E_{q_{\lambda}(z)} \left[ \log p(z,D|\theta) - \log q_{\lambda}(z) \right]$ (using results above)
	- so, instead of computing the true posterior in the E step, we can fit an approximate posterior simply by maximizing ELBO w.r.t. $\lambda$
	- TLDR; maximize ELBO w.r.t. $\lambda$
- *M step*
	- assume $\lambda$ is fixed
	- the M steps involves maximizing the likelihood w.r.t. $\theta$ - this is in fact equivalent to maximizing ELBO w.r.t. $\theta$
	- TLDR; maximize ELBO w.r.t. $\theta$