# EMA Hourly Continuation — POL/USDT P20_21

**Symbol:** POL/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 141 |
| net_profit_factor | 0.4805 |
| net_win_rate | 0.4184 |
| gross_profit_factor | 0.6971 |
| gross_win_rate | 0.4184 |
| sharpe_ratio | -2.5269 |
| sortino_ratio | -0.4279 |
| max_drawdown | 0.4105 |
| cagr | -0.1784 |
| net_avg_win | 61.0680 |
| net_avg_loss | -91.4421 |
| avg_hold_time_bars | 5.0426 |
| exposure | 0.0323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
