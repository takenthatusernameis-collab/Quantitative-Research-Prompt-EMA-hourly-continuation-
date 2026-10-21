# EMA Hourly Continuation — XTZ/USDT P21_89

**Symbol:** XTZ/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.7145 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9621 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -2.5821 |
| sortino_ratio | -0.8458 |
| max_drawdown | 0.6419 |
| cagr | -0.3214 |
| net_avg_win | 61.3127 |
| net_avg_loss | -80.7271 |
| avg_hold_time_bars | 17.2519 |
| exposure | 0.4109 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
