# EMA Hourly Continuation — CRO/USDT P21_144

**Symbol:** CRO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.5723 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 1.0078 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -3.7208 |
| sortino_ratio | -1.1134 |
| max_drawdown | 0.7643 |
| cagr | -0.4248 |
| net_avg_win | 45.4566 |
| net_avg_loss | -72.5317 |
| avg_hold_time_bars | 27.6998 |
| exposure | 0.5830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
