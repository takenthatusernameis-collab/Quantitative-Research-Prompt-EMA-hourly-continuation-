# EMA Hourly Continuation — IOTA/USDT P20_50

**Symbol:** IOTA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.7216 |
| net_win_rate | 0.4877 |
| gross_profit_factor | 0.9803 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -2.5812 |
| sortino_ratio | -0.8489 |
| max_drawdown | 0.6510 |
| cagr | -0.3211 |
| net_avg_win | 62.7181 |
| net_avg_loss | -82.7300 |
| avg_hold_time_bars | 7.5769 |
| exposure | 0.1815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
