# EMA Hourly Continuation — RUNE/USDT P21_55

**Symbol:** RUNE/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.8124 |
| net_win_rate | 0.5267 |
| gross_profit_factor | 1.1122 |
| gross_win_rate | 0.5267 |
| sharpe_ratio | -1.5226 |
| sortino_ratio | -0.4931 |
| max_drawdown | 0.4506 |
| cagr | -0.2029 |
| net_avg_win | 70.6842 |
| net_avg_loss | -96.8389 |
| avg_hold_time_bars | 8.3960 |
| exposure | 0.1927 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
