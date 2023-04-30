from diffusers import StableDiffusionOnnxPipeline
import torch
from diffusers import (
    DDPMScheduler,
    DDIMScheduler,
    PNDMScheduler,
    LMSDiscreteScheduler,
    EulerDiscreteScheduler,
    EulerAncestralDiscreteScheduler,
    DPMSolverMultistepScheduler
)

scheduler = DPMSolverMultistepScheduler.from_pretrained("./stable-diffusion-v1-5", subfolder="scheduler")

pipe = StableDiffusionOnnxPipeline.from_pretrained(
    './stable-diffusion-v1-5',
    custom_pipeline="./pipeline",
    revision="onnx",
    scheduler=scheduler,
    safety_checker=None,
    provider="CPUExecutionProvider",
)


prompt = "fully body fantasy female, heavenly, epic, highly detailed, by russ mills, by josephine wall, by Edwin Deakin"
neg_prompt = "lowres, bad anatomy, error body, error hair, error arm, error hands, bad hands, error fingers, bad fingers, missing fingers, error legs, bad legs, multiple legs, missing legs, error lighting, error shadow, error reflection, text, error, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry"
                                                                                                                       
generator = torch.Generator(device="cpu").manual_seed(1)



image = pipe.text2img(prompt,negative_prompt=neg_prompt, num_inference_steps=8, width=320, height=512, guidance_scale=10, generator=generator, max_embeddings_multiples=3).images[0]
image.save('./test.png')
