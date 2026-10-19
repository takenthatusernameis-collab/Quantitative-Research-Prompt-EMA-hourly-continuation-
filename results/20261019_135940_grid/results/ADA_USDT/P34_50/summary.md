# EMA Hourly Continuation — ADA/USDT P34_50

**Symbol:** ADA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 897 |
| net_profit_factor | 0.2871 |
| net_win_rate | 0.3980 |
| gross_profit_factor | 0.7294 |
| gross_win_rate | 0.4292 |
| sharpe_ratio | -10.5694 |
| sortino_ratio | -4.5507 |
| max_drawdown | 0.9970 |
| cagr | -0.9012 |
| net_avg_win | 11.2492 |
| net_avg_loss | -25.9001 |
| avg_hold_time_bars | 2.5284 |
| exposure | 0.1031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
