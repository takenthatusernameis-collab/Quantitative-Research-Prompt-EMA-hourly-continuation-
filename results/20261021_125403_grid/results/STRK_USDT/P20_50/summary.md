# EMA Hourly Continuation — STRK/USDT P20_50

**Symbol:** STRK/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.7685 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 0.9829 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -1.8028 |
| sortino_ratio | -0.5654 |
| max_drawdown | 0.4899 |
| cagr | -0.2286 |
| net_avg_win | 66.8159 |
| net_avg_loss | -85.8581 |
| avg_hold_time_bars | 7.4405 |
| exposure | 0.1620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
