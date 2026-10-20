# EMA Hourly Continuation — MEME/USDT P8_55

**Symbol:** MEME/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1030 |
| net_profit_factor | 0.6685 |
| net_win_rate | 0.4845 |
| gross_profit_factor | 0.9873 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -4.5042 |
| sortino_ratio | -2.0405 |
| max_drawdown | 0.9165 |
| cagr | -0.6200 |
| net_avg_win | 36.8570 |
| net_avg_loss | -51.8099 |
| avg_hold_time_bars | 10.5369 |
| exposure | 0.4933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
