# EMA Hourly Continuation — HTX/USDT P20_21

**Symbol:** HTX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1375 |
| net_profit_factor | 0.0394 |
| net_win_rate | 0.1338 |
| gross_profit_factor | 0.2711 |
| gross_win_rate | 0.2625 |
| sharpe_ratio | -25.8598 |
| sortino_ratio | -17.0710 |
| max_drawdown | 1.0000 |
| cagr | -0.9999 |
| net_avg_win | 2.2295 |
| net_avg_loss | -8.7407 |
| avg_hold_time_bars | 2.1578 |
| exposure | 0.1343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
