# EMA Hourly Continuation — IMX/USDT P55_200

**Symbol:** IMX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 1.0081 |
| net_win_rate | 0.5487 |
| gross_profit_factor | 1.2039 |
| gross_win_rate | 0.5487 |
| sharpe_ratio | 0.0943 |
| sortino_ratio | 0.0227 |
| max_drawdown | 0.1387 |
| cagr | 0.0044 |
| net_avg_win | 90.9888 |
| net_avg_loss | -109.7514 |
| avg_hold_time_bars | 31.9675 |
| exposure | 0.4007 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
