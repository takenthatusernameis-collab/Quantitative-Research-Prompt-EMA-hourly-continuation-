# EMA Hourly Continuation — CTC/USDT P8_26

**Symbol:** CTC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1495 |
| net_profit_factor | 0.4033 |
| net_win_rate | 0.4395 |
| gross_profit_factor | 0.8965 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -10.5332 |
| sortino_ratio | -5.7434 |
| max_drawdown | 0.9993 |
| cagr | -0.9432 |
| net_avg_win | 10.2780 |
| net_avg_loss | -19.9823 |
| avg_hold_time_bars | 4.5425 |
| exposure | 0.3087 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
