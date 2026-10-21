# EMA Hourly Continuation — AVA/USDT P20_89

**Symbol:** AVA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.8821 |
| net_win_rate | 0.5326 |
| gross_profit_factor | 1.1185 |
| gross_win_rate | 0.5326 |
| sharpe_ratio | -0.7639 |
| sortino_ratio | -0.2404 |
| max_drawdown | 0.3349 |
| cagr | -0.1082 |
| net_avg_win | 73.8789 |
| net_avg_loss | -95.4488 |
| avg_hold_time_bars | 15.5368 |
| exposure | 0.3355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
