# EMA Hourly Continuation — JTO/USDT P20_144

**Symbol:** JTO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.7887 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.9180 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -1.6152 |
| sortino_ratio | -0.4625 |
| max_drawdown | 0.4784 |
| cagr | -0.1927 |
| net_avg_win | 80.4439 |
| net_avg_loss | -92.4134 |
| avg_hold_time_bars | 29.0936 |
| exposure | 0.5369 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
