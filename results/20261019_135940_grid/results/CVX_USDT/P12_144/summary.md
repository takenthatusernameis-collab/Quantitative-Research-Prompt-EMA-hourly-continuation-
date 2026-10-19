# EMA Hourly Continuation — CVX/USDT P12_144

**Symbol:** CVX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.6034 |
| net_win_rate | 0.4548 |
| gross_profit_factor | 0.8374 |
| gross_win_rate | 0.4645 |
| sharpe_ratio | -3.0757 |
| sortino_ratio | -0.8632 |
| max_drawdown | 0.6573 |
| cagr | -0.3446 |
| net_avg_win | 53.4869 |
| net_avg_loss | -73.9349 |
| avg_hold_time_bars | 38.1076 |
| exposure | 0.7085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
