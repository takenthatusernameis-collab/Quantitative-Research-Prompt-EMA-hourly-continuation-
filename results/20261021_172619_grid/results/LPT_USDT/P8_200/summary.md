# EMA Hourly Continuation — LPT/USDT P8_200

**Symbol:** LPT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.7304 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.8630 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -1.7570 |
| sortino_ratio | -0.4591 |
| max_drawdown | 0.4475 |
| cagr | -0.1906 |
| net_avg_win | 70.6569 |
| net_avg_loss | -84.4426 |
| avg_hold_time_bars | 50.3451 |
| exposure | 0.7758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
