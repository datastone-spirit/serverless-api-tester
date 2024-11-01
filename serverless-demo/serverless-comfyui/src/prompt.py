prompt_text = r'''
{
  "3": {
    "inputs": {
      "seed": 1071208483241017,
      "steps": 30,
      "cfg": 5.45,
      "sampler_name": "euler",
      "scheduler": "sgm_uniform",
      "denoise": 1,
      "model": [
        "4",
        0
      ],
      "positive": [
        "16",
        0
      ],
      "negative": [
        "40",
        0
      ],
      "latent_image": [
        "53",
        0
      ]
    },
    "class_type": "KSampler",
    "_meta": {
      "title": "KSampler"
    }
  },
  "4": {
    "inputs": {
      "ckpt_name": "sd3.5_large_fp8_scaled.safetensors"
    },
    "class_type": "CheckpointLoaderSimple",
    "_meta": {
      "title": "Load Checkpoint"
    }
  },
  "8": {
    "inputs": {
      "samples": [
        "3",
        0
      ],
      "vae": [
        "4",
        2
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE Decode"
    }
  },
  "9": {
    "inputs": {
      "filename_prefix": "ComfyUI",
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveImage",
    "_meta": {
      "title": "Save Image"
    }
  },
  "16": {
    "inputs": {
      "text": "",
      "clip": [
        "43",
        0
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "Positive Prompt"
    }
  },
  "40": {
    "inputs": {
      "text": "",
      "clip": [
        "43",
        0
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "Negative Prompt"
    }
  },
  "43": {
    "inputs": {
      "clip_name1": "clip_l.safetensors",
      "clip_name2": "clip_g.safetensors",
      "clip_name3": "t5xxl_fp8_e4m3fn_scaled.safetensors"
    },
    "class_type": "TripleCLIPLoader",
    "_meta": {
      "title": "TripleCLIPLoader"
    }
  },
  "53": {
    "inputs": {
      "width": 512,
      "height": 512,
      "batch_size": 1
    },
    "class_type": "EmptySD3LatentImage",
    "_meta": {
      "title": "EmptySD3LatentImage"
    }
  }
}
'''