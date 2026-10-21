# EMA Hourly Continuation — MEME/USDT P26_200

**Symbol:** MEME/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.8882 |
| net_win_rate | 0.5151 |
| gross_profit_factor | 1.0526 |
| gross_win_rate | 0.5151 |
| sharpe_ratio | -0.6093 |
| sortino_ratio | -0.1514 |
| max_drawdown | 0.2766 |
| cagr | -0.0699 |
| net_avg_win | 85.7885 |
| net_avg_loss | -102.5801 |
| avg_hold_time_bars | 45.7090 |
| exposure | 0.6212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
