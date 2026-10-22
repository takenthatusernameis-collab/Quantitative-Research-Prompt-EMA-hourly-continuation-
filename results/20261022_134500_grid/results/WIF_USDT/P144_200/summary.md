# EMA Hourly Continuation — WIF/USDT P144_200

**Symbol:** WIF/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.5000 |
| net_win_rate | 0.4575 |
| gross_profit_factor | 0.8595 |
| gross_win_rate | 0.4750 |
| sharpe_ratio | -4.0113 |
| sortino_ratio | -1.1384 |
| max_drawdown | 0.7625 |
| cagr | -0.4183 |
| net_avg_win | 40.6213 |
| net_avg_loss | -68.5174 |
| avg_hold_time_bars | 3.9225 |
| exposure | 0.0713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
