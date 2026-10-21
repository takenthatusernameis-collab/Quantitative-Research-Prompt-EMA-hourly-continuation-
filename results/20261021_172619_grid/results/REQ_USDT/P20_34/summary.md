# EMA Hourly Continuation — REQ/USDT P20_34

**Symbol:** REQ/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.5135 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.8739 |
| gross_win_rate | 0.4433 |
| sharpe_ratio | -5.3453 |
| sortino_ratio | -1.6783 |
| max_drawdown | 0.8617 |
| cagr | -0.5419 |
| net_avg_win | 43.1841 |
| net_avg_loss | -66.3943 |
| avg_hold_time_bars | 5.8718 |
| exposure | 0.1270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
