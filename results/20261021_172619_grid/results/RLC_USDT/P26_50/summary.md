# EMA Hourly Continuation — RLC/USDT P26_50

**Symbol:** RLC/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.6352 |
| net_win_rate | 0.4701 |
| gross_profit_factor | 0.9024 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -3.2703 |
| sortino_ratio | -1.0122 |
| max_drawdown | 0.6991 |
| cagr | -0.3711 |
| net_avg_win | 54.4437 |
| net_avg_loss | -76.0397 |
| avg_hold_time_bars | 5.9487 |
| exposure | 0.1265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
