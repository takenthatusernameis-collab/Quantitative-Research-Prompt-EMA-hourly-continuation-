# EMA Hourly Continuation — LQTY/USDT P20_144

**Symbol:** LQTY/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.6477 |
| net_win_rate | 0.4692 |
| gross_profit_factor | 0.8749 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -2.8975 |
| sortino_ratio | -0.8868 |
| max_drawdown | 0.6574 |
| cagr | -0.3399 |
| net_avg_win | 54.0191 |
| net_avg_loss | -73.7269 |
| avg_hold_time_bars | 27.8535 |
| exposure | 0.5936 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
