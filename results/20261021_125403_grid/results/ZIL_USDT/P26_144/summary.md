# EMA Hourly Continuation — ZIL/USDT P26_144

**Symbol:** ZIL/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.8641 |
| net_win_rate | 0.5251 |
| gross_profit_factor | 1.0973 |
| gross_win_rate | 0.5251 |
| sharpe_ratio | -0.8695 |
| sortino_ratio | -0.2436 |
| max_drawdown | 0.3533 |
| cagr | -0.1088 |
| net_avg_win | 80.2064 |
| net_avg_loss | -102.6225 |
| avg_hold_time_bars | 27.6649 |
| exposure | 0.4766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
