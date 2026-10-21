# EMA Hourly Continuation — MEME/USDT P34_200

**Symbol:** MEME/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.8697 |
| net_win_rate | 0.5084 |
| gross_profit_factor | 1.0269 |
| gross_win_rate | 0.5084 |
| sharpe_ratio | -0.7030 |
| sortino_ratio | -0.1744 |
| max_drawdown | 0.2102 |
| cagr | -0.0793 |
| net_avg_win | 82.2416 |
| net_avg_loss | -97.7831 |
| avg_hold_time_bars | 39.4415 |
| exposure | 0.5360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
