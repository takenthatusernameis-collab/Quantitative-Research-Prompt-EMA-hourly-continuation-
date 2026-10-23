# EMA Hourly Continuation — BOSON/USDT P55_200

**Symbol:** BOSON/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.7650 |
| net_win_rate | 0.4875 |
| gross_profit_factor | 0.9634 |
| gross_win_rate | 0.4875 |
| sharpe_ratio | -1.7893 |
| sortino_ratio | -0.5345 |
| max_drawdown | 0.4626 |
| cagr | -0.2191 |
| net_avg_win | 70.0318 |
| net_avg_loss | -87.0904 |
| avg_hold_time_bars | 16.9184 |
| exposure | 0.3391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
