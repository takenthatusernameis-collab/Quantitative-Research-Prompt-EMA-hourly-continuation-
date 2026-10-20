# EMA Hourly Continuation — CETUS/USDT P26_100

**Symbol:** CETUS/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.7139 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 1.0052 |
| gross_win_rate | 0.4861 |
| sharpe_ratio | -3.3178 |
| sortino_ratio | -1.1912 |
| max_drawdown | 0.7707 |
| cagr | -0.4312 |
| net_avg_win | 61.1075 |
| net_avg_loss | -78.5040 |
| avg_hold_time_bars | 12.2299 |
| exposure | 0.3586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
