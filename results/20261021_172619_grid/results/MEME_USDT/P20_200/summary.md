# EMA Hourly Continuation — MEME/USDT P20_200

**Symbol:** MEME/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.8957 |
| net_win_rate | 0.5172 |
| gross_profit_factor | 1.0624 |
| gross_win_rate | 0.5172 |
| sharpe_ratio | -0.5907 |
| sortino_ratio | -0.1516 |
| max_drawdown | 0.2611 |
| cagr | -0.0703 |
| net_avg_win | 87.1179 |
| net_avg_loss | -104.2067 |
| avg_hold_time_bars | 44.9561 |
| exposure | 0.6519 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
