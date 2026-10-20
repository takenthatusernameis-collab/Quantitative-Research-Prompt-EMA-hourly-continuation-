# EMA Hourly Continuation — MEME/USDT P26_50

**Symbol:** MEME/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1014 |
| net_profit_factor | 0.4938 |
| net_win_rate | 0.4448 |
| gross_profit_factor | 0.8853 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -7.4840 |
| sortino_ratio | -3.3645 |
| max_drawdown | 0.9840 |
| cagr | -0.8044 |
| net_avg_win | 21.2748 |
| net_avg_loss | -34.5096 |
| avg_hold_time_bars | 3.4103 |
| exposure | 0.1572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
