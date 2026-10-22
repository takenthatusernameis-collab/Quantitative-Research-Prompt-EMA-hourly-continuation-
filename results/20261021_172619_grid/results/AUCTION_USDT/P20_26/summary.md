# EMA Hourly Continuation — AUCTION/USDT P20_26

**Symbol:** AUCTION/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.4851 |
| net_win_rate | 0.4297 |
| gross_profit_factor | 0.7691 |
| gross_win_rate | 0.4324 |
| sharpe_ratio | -4.6311 |
| sortino_ratio | -1.2849 |
| max_drawdown | 0.7859 |
| cagr | -0.4534 |
| net_avg_win | 45.4840 |
| net_avg_loss | -70.6457 |
| avg_hold_time_bars | 5.2467 |
| exposure | 0.0895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
