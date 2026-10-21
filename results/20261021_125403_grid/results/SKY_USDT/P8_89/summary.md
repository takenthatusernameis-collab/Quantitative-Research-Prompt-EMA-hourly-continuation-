# EMA Hourly Continuation — SKY/USDT P8_89

**Symbol:** SKY/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.7571 |
| net_win_rate | 0.4860 |
| gross_profit_factor | 0.9589 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -2.2737 |
| sortino_ratio | -0.7733 |
| max_drawdown | 0.6019 |
| cagr | -0.3005 |
| net_avg_win | 71.5689 |
| net_avg_loss | -89.3860 |
| avg_hold_time_bars | 23.2409 |
| exposure | 0.6026 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
