# EMA Hourly Continuation — BOME/USDT P8_26

**Symbol:** BOME/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1536 |
| net_profit_factor | 0.4893 |
| net_win_rate | 0.4609 |
| gross_profit_factor | 0.8461 |
| gross_win_rate | 0.4727 |
| sharpe_ratio | -8.1328 |
| sortino_ratio | -4.4662 |
| max_drawdown | 0.9961 |
| cagr | -0.8880 |
| net_avg_win | 13.4790 |
| net_avg_loss | -23.5533 |
| avg_hold_time_bars | 3.6315 |
| exposure | 0.2535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
