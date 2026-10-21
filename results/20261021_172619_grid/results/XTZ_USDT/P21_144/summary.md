# EMA Hourly Continuation — XTZ/USDT P21_144

**Symbol:** XTZ/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.8171 |
| net_win_rate | 0.5097 |
| gross_profit_factor | 1.0464 |
| gross_win_rate | 0.5097 |
| sharpe_ratio | -1.2082 |
| sortino_ratio | -0.3296 |
| max_drawdown | 0.3607 |
| cagr | -0.1415 |
| net_avg_win | 77.2506 |
| net_avg_loss | -98.2844 |
| avg_hold_time_bars | 35.9391 |
| exposure | 0.5897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
