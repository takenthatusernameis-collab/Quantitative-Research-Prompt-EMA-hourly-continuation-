# EMA Hourly Continuation — POLYX/USDT P20_50

**Symbol:** POLYX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 591 |
| net_profit_factor | 0.7089 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 0.9908 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -2.8277 |
| sortino_ratio | -0.9843 |
| max_drawdown | 0.6992 |
| cagr | -0.3636 |
| net_avg_win | 56.3884 |
| net_avg_loss | -78.2111 |
| avg_hold_time_bars | 7.3841 |
| exposure | 0.1984 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
