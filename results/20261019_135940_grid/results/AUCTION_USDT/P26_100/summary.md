# EMA Hourly Continuation — AUCTION/USDT P26_100

**Symbol:** AUCTION/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.5809 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.9074 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -4.8810 |
| sortino_ratio | -1.7839 |
| max_drawdown | 0.8919 |
| cagr | -0.5760 |
| net_avg_win | 39.4515 |
| net_avg_loss | -57.5507 |
| avg_hold_time_bars | 11.7832 |
| exposure | 0.3616 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
