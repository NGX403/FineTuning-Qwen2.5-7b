{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/data/miniconda/envs/torch/lib/python3.10/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html\n",
      "  from .autonotebook import tqdm as notebook_tqdm\n",
      "Loading checkpoint shards: 100%|██████████| 4/4 [00:18<00:00,  4.75s/it]\n",
      "Some parameters are on the meta device device because they were offloaded to the cpu.\n",
      "The attention mask is not set and cannot be inferred from input because pad token is same as eos token.As a consequence, you may observe unexpected behavior. Please pass your input's `attention_mask` to obtain reliable results.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "system> 我是来自阿里云的大规模语言模型，我叫通义千问。我可以提供法律"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Exception ignored in: <bound method IPythonKernel._clean_thread_parent_frames of <ipykernel.ipkernel.IPythonKernel object at 0x7f047ec85180>>\n",
      "Traceback (most recent call last):\n",
      "  File \"/data/miniconda/envs/torch/lib/python3.10/site-packages/ipykernel/ipkernel.py\", line 775, in _clean_thread_parent_frames\n",
      "    def _clean_thread_parent_frames(\n",
      "KeyboardInterrupt: \n"
     ]
    }
   ],
   "source": [
    "\n",
    "from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer\n",
    "\n",
    "device =\"cuda\" # the device to load the model onto \n",
    "\n",
    "def get_stream_response(model, tokenizer, messages): \n",
    "\n",
    "    text = tokenizer.apply_chat_template(\n",
    "        messages, \n",
    "        tokenize=False, \n",
    "        add_generation_prompt=True\n",
    "    ) \n",
    "\n",
    "    model_inputs = tokenizer([text], return_tensors=\"pt\"). to(device)\n",
    "    streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)\n",
    "\n",
    "    def generate_with_stream():\n",
    "\n",
    "        for output in model. generate(model_inputs.input_ids, max_new_tokens=512,streamer=streamer): \n",
    "            yield output \n",
    "    return generate_with_stream() \n",
    "\n",
    "\n",
    "def chat(model, tokenizer): \n",
    "\n",
    "    prompt=\"你是谁？\"\n",
    "    messages = [\n",
    "        {\"role\":\"system\",\"content\":\"你是一个法律知识助手，只负责回答用户提出的法律问题\"},\n",
    "        {\"role\": \"user\", \"content\": prompt}\n",
    "    ]\n",
    "    legal_prompt =\"\"\"\n",
    "        作为一位专业的法律知识助手，仅当问题和法律相关时才作答。\n",
    "        否则，请回复：“我只能提供法律相关的咨询，请提出与法律有关的问题。”\n",
    "        用户问题： \"\"\"\n",
    "\n",
    "    while True: \n",
    "        print(\"system> \",end=\"\")\n",
    "        response_gen = get_stream_response(model, tokenizer, messages)\n",
    "        response_text =\"\"\n",
    "\n",
    "        for _ in response_gen:\n",
    "            pass\n",
    "\n",
    "        messages. append({\"role\": \"system\", \"content\": response_text})\n",
    "        prompt = input(\"user>\")\n",
    "\n",
    "        if prompt ==\" exit\":\n",
    "            break\n",
    "\n",
    "        messages. append({\"role\": \"user\", \"content\": legal_prompt + prompt})\n",
    "\n",
    "model_name_or_path ='Qwen2.5-7B-Instruct'\n",
    "model = AutoModelForCausalLM. from_pretrained(\n",
    "    model_name_or_path,\n",
    "    torch_dtype=\"auto\",\n",
    "    device_map=\"auto\"\n",
    ")\n",
    "\n",
    "tokenizer = AutoTokenizer. from_pretrained(model_name_or_path)\n",
    "chat(model, tokenizer) "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "torch",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
