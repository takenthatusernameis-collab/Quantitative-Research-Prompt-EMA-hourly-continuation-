# EMA Hourly Continuation — EWT/USDT P12_26

**Symbol:** EWT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1215 |
| net_profit_factor | 0.3114 |
| net_win_rate | 0.3481 |
| gross_profit_factor | 0.6310 |
| gross_win_rate | 0.3737 |
| sharpe_ratio | -13.8718 |
| sortino_ratio | -6.9285 |
| max_drawdown | 0.9999 |
| cagr | -0.9738 |
| net_avg_win | 10.6878 |
| net_avg_loss | -18.3332 |
| avg_hold_time_bars | 3.2782 |
| exposure | 0.1810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
