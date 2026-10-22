# EMA Hourly Continuation — HTX/USDT P55_100

**Symbol:** HTX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.2081 |
| net_win_rate | 0.2741 |
| gross_profit_factor | 0.6215 |
| gross_win_rate | 0.3566 |
| sharpe_ratio | -13.1671 |
| sortino_ratio | -5.2731 |
| max_drawdown | 0.9992 |
| cagr | -0.9413 |
| net_avg_win | 13.3966 |
| net_avg_loss | -24.3119 |
| avg_hold_time_bars | 6.0168 |
| exposure | 0.1947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
