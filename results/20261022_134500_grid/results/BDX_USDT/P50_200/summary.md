# EMA Hourly Continuation — BDX/USDT P50_200

**Symbol:** BDX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 870 |
| net_profit_factor | 0.3155 |
| net_win_rate | 0.3322 |
| gross_profit_factor | 0.6970 |
| gross_win_rate | 0.3828 |
| sharpe_ratio | -12.6546 |
| sortino_ratio | -5.4123 |
| max_drawdown | 0.9994 |
| cagr | -0.9478 |
| net_avg_win | 15.9393 |
| net_avg_loss | -25.1299 |
| avg_hold_time_bars | 7.7276 |
| exposure | 0.3056 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
