# EMA Hourly Continuation — NEO/USDT P8_100

**Symbol:** NEO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.6058 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9714 |
| gross_win_rate | 0.4972 |
| sharpe_ratio | -3.5125 |
| sortino_ratio | -1.1479 |
| max_drawdown | 0.7702 |
| cagr | -0.4241 |
| net_avg_win | 44.1539 |
| net_avg_loss | -67.4565 |
| avg_hold_time_bars | 29.6335 |
| exposure | 0.7314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
