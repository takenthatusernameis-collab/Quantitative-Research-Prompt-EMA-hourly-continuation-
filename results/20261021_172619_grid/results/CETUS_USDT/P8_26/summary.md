# EMA Hourly Continuation — CETUS/USDT P8_26

**Symbol:** CETUS/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 753 |
| net_profit_factor | 0.7535 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 0.9834 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -2.6574 |
| sortino_ratio | -1.0409 |
| max_drawdown | 0.7064 |
| cagr | -0.3800 |
| net_avg_win | 57.8671 |
| net_avg_loss | -74.1930 |
| avg_hold_time_bars | 6.2005 |
| exposure | 0.2113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
