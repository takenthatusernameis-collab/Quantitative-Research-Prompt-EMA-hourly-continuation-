# EMA Hourly Continuation — KAS/USDT P8_21

**Symbol:** KAS/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.8399 |
| net_win_rate | 0.5330 |
| gross_profit_factor | 1.1414 |
| gross_win_rate | 0.5330 |
| sharpe_ratio | -1.2322 |
| sortino_ratio | -0.3857 |
| max_drawdown | 0.4334 |
| cagr | -0.1633 |
| net_avg_win | 75.7606 |
| net_avg_loss | -102.9682 |
| avg_hold_time_bars | 5.8593 |
| exposure | 0.1249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
