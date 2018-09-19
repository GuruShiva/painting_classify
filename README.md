# What Painting Is This?

_Update- This project won for #SchoolofAIVancouver Image Classification Code Challenge 1 ->https://www.linkedin.com/feed/update/urn:li:activity:6448031863524204544_

This project was created for #SchoolofAIVancouver Image Classification Code Challenge 1. This image classification tries to classify paintings into 4 classes:

* Impressionism

![Starry Night](/common/starry_night.jpg "Starry Night By Vincent Van Gogh")

* Expressionism

![Expressionist Woman](/common/expressionist-woman.jpg "Expressionist Woman")


* Fauvism

![Matisse Woman](/common/matisse-woman-with-a-hat.jpg  "Mattise Woman With A Hat By Henri Mattise")


* Modern Abstract

![Modern Abstract Painting](/common/modern_abstract_1.jpg  "Modern Abstract Painting")


## Getting Started

You can clone the repo to retrain and test the model. However please not that there arent any 'train' data in this repo. It has been removed to avoid uploading all the images to git.

There are a couple 'test' data for testing purposes.

The `retrain.py` was run by the following config:

```

python src/retrain.py \
    --bottleneck_dir tf_files/bottlenecks \
    --image_dir tf_files/data/train \
    --tfhub_module https://tfhub.dev/google/imagenet/mobilenet_v1_075_160/feature_vector/1 \
    --how_many_training_steps 100 \
    --train_batch_size 500 \
    --validation_batch_size 300 \
    --summaries_dir tf_files/retrain_logs \
    --output_graph tf_files/output_graph.pb \
    --output_labels tf_files/output_labels.txt
```

### Prerequisites

You will need these tools installed before using the `get_train_data.py` and `get_test_data.py`

* [GoogleImagesDownload](https://github.com/hardikvasa/google-images-download)
* ChromeDriver 




## Built With

* [Python3](https://www.python.org/about/) - The programming language used
* [TensorFlow](https://www.tensorflow.org/) - Opensource Machine Learning Framework


## Known Bugs

There are some known issues in this repo for `get_train_data.py` and `get_test_data.py`. These issues can be fixed manually. 

*Issue 1- Often the image scraper downloads images that are not '.jpg' which leads to the `retrain.py` to give an error.Deleting the particular image solves the issue ;)

*Issue 2- The image scraper downloads the images with the image file name as it is. The `retrain.py` does not take file with long file names. Simply renaming the file fixes this issue. 


## Disclaimer

The trained model in this image classifier is not perfect! The data used in this project was scraped from the Internet. The dataset has not gone through rigorous data cleaning or parameter tuning techniques and there maybe some false positives during the labelling test. Feel free to retrain the model with a more accurate dataset.

## Authors

* **Guru Shiva** - *Initial work* 



## License

This project is licensed under the MIT License

## Acknowledgments

* [Siraj Raval](https://github.com/llSourcell) for ML/AI inspiration and starting School of AI
* [Akshi Chaudary](https://github.com/akshi8)- SchoolofAIVancouver
* [Johannes Harmse](https://github.com/johannesharmse)- SchoolofAIVancouver
* [Xinbin Haung](https://github.com/xinbinhuang)- SchoolofAIVancouver
* [Billie Thompson](https://github.com/PurpleBooth)- For this amazing README.md template
* The Internet 