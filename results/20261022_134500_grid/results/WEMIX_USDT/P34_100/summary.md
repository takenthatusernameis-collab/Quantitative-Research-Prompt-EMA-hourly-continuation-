# EMA Hourly Continuation — WEMIX/USDT P34_100

**Symbol:** WEMIX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1030 |
| net_profit_factor | 0.2612 |
| net_win_rate | 0.3000 |
| gross_profit_factor | 0.4426 |
| gross_win_rate | 0.3117 |
| sharpe_ratio | -13.2446 |
| sortino_ratio | -6.1071 |
| max_drawdown | 0.9995 |
| cagr | -0.9531 |
| net_avg_win | 11.4363 |
| net_avg_loss | -18.7645 |
| avg_hold_time_bars | 7.1194 |
| exposure | 0.3333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
