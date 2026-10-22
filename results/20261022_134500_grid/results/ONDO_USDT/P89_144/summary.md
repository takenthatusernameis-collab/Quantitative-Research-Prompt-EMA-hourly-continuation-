# EMA Hourly Continuation — ONDO/USDT P89_144

**Symbol:** ONDO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 558 |
| net_profit_factor | 0.4806 |
| net_win_rate | 0.4337 |
| gross_profit_factor | 0.7900 |
| gross_win_rate | 0.4373 |
| sharpe_ratio | -5.5991 |
| sortino_ratio | -1.8773 |
| max_drawdown | 0.8967 |
| cagr | -0.5936 |
| net_avg_win | 34.2565 |
| net_avg_loss | -54.5815 |
| avg_hold_time_bars | 4.4050 |
| exposure | 0.1117 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
