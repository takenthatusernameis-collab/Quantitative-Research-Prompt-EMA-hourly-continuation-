# EMA Hourly Continuation — ENJ/USDT P100_144

**Symbol:** ENJ/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 229 |
| net_profit_factor | 0.6644 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.8954 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -2.0415 |
| sortino_ratio | -0.4404 |
| max_drawdown | 0.4604 |
| cagr | -0.1832 |
| net_avg_win | 73.9708 |
| net_avg_loss | -97.6432 |
| avg_hold_time_bars | 7.4934 |
| exposure | 0.0777 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
