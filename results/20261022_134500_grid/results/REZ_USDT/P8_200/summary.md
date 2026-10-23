# EMA Hourly Continuation — REZ/USDT P8_200

**Symbol:** REZ/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.8217 |
| net_win_rate | 0.5094 |
| gross_profit_factor | 1.0313 |
| gross_win_rate | 0.5117 |
| sharpe_ratio | -1.2080 |
| sortino_ratio | -0.3594 |
| max_drawdown | 0.4078 |
| cagr | -0.1546 |
| net_avg_win | 72.1969 |
| net_avg_loss | -91.2270 |
| avg_hold_time_bars | 39.3052 |
| exposure | 0.7725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
