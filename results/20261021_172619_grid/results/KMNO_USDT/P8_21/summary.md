# EMA Hourly Continuation — KMNO/USDT P8_21

**Symbol:** KMNO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 592 |
| net_profit_factor | 0.7859 |
| net_win_rate | 0.5220 |
| gross_profit_factor | 1.0903 |
| gross_win_rate | 0.5220 |
| sharpe_ratio | -1.8936 |
| sortino_ratio | -0.6671 |
| max_drawdown | 0.5389 |
| cagr | -0.2660 |
| net_avg_win | 63.4841 |
| net_avg_loss | -88.2010 |
| avg_hold_time_bars | 5.7399 |
| exposure | 0.1569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
