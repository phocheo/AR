# AR Card - A Support Project for our dear, People's Artist Tu Long

## Motivations

We have gifted the community some cards of our idol in 2 previous nights of concert. Here are our conclusions.

First, people will rarely care about the cards again, they maybe will keep them in a binder forever. Worse, they even throw cards away in the concert.

Second, there are a lot of cards in the concert day, how we can stand out from them?

The card is the image of our idol, of course we want people will love his card and impressed by him.

An idea popped in our mind, what about immigrating state-of-the-art technology into our gifts?

So, that is why this repository exists (it isn't SOTA technology btw).

## How-to?

It took me a research to come to this current state. There are some problems I have when doing this project:

- I haven't experienced any AR services before
- There exists AR Card by Idol Company, but also, I don't know how they work (and I forgot to research this too)
- I have little experience with real-life products

After the research, I realize it can cost us a fortune to outsource the technology part (not really that much money but still a lot to us).

My ego just hits, I am a Computer Engineer, how can't I do a project with such simple workflow?

I read some posts on StackOverflow, I think about the power of `threejs` and `arjs`.

The product will be something like this:

- A website to detect the marker of AR card (host free on GitHub)
- When the marker is detect, the video of my idol will appear on a defined plane

Easy, isn't it?

Then another problem comes: **I have absolute zero knowledge and experience with web development**

Thanks god, I have found the [AR-examples](https://github.com/stemkoski/AR-Examples) by `stemkoski`.

My job now is re-use the structure of their code and modify to suit my need.

## Results

I guess it works (after a series of ping pong badadum hotfix)?
