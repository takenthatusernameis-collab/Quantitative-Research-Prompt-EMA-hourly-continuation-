# EMA Hourly Continuation — XYO/USDT P50_100

**Symbol:** XYO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.4175 |
| net_win_rate | 0.4046 |
| gross_profit_factor | 0.8226 |
| gross_win_rate | 0.4292 |
| sharpe_ratio | -8.1702 |
| sortino_ratio | -3.1306 |
| max_drawdown | 0.9814 |
| cagr | -0.7939 |
| net_avg_win | 23.6814 |
| net_avg_loss | -38.5521 |
| avg_hold_time_bars | 6.2166 |
| exposure | 0.2065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
