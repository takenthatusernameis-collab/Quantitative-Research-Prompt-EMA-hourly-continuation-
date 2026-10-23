# EMA Hourly Continuation — MEME/USDT P55_89

**Symbol:** MEME/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.5224 |
| net_win_rate | 0.4655 |
| gross_profit_factor | 0.8809 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -5.2659 |
| sortino_ratio | -1.9406 |
| max_drawdown | 0.9087 |
| cagr | -0.6108 |
| net_avg_win | 31.2823 |
| net_avg_loss | -52.1472 |
| avg_hold_time_bars | 4.6197 |
| exposure | 0.1430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
