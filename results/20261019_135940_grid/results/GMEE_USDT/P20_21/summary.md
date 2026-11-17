# EMA Hourly Continuation — GMEE/USDT P20_21

**Symbol:** GMEE/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1224 |
| net_profit_factor | 0.1742 |
| net_win_rate | 0.2900 |
| gross_profit_factor | 0.5085 |
| gross_win_rate | 0.3374 |
| sharpe_ratio | -17.5476 |
| sortino_ratio | -9.1392 |
| max_drawdown | 1.0000 |
| cagr | -0.9941 |
| net_avg_win | 5.9420 |
| net_avg_loss | -13.9349 |
| avg_hold_time_bars | 1.9150 |
| exposure | 0.1065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
