# EMA Hourly Continuation — UQC/USDT P12_50

**Symbol:** UQC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.2372 |
| net_win_rate | 0.3109 |
| gross_profit_factor | 0.4841 |
| gross_win_rate | 0.3284 |
| sharpe_ratio | -7.4975 |
| sortino_ratio | -2.1081 |
| max_drawdown | 0.9345 |
| cagr | -0.6604 |
| net_avg_win | 23.2500 |
| net_avg_loss | -44.2244 |
| avg_hold_time_bars | 35.2090 |
| exposure | 0.6406 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
