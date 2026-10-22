# EMA Hourly Continuation — MANA/USDT P89_100

**Symbol:** MANA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.2376 |
| net_win_rate | 0.3723 |
| gross_profit_factor | 0.7515 |
| gross_win_rate | 0.4299 |
| sharpe_ratio | -10.6117 |
| sortino_ratio | -3.9475 |
| max_drawdown | 0.9956 |
| cagr | -0.8827 |
| net_avg_win | 12.9831 |
| net_avg_loss | -32.3993 |
| avg_hold_time_bars | 1.9190 |
| exposure | 0.0560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
