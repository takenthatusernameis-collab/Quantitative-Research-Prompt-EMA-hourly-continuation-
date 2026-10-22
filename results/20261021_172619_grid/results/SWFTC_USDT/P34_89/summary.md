# EMA Hourly Continuation — SWFTC/USDT P34_89

**Symbol:** SWFTC/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.7587 |
| net_win_rate | 0.4957 |
| gross_profit_factor | 0.9890 |
| gross_win_rate | 0.4957 |
| sharpe_ratio | -1.6630 |
| sortino_ratio | -0.4438 |
| max_drawdown | 0.4038 |
| cagr | -0.1847 |
| net_avg_win | 73.3378 |
| net_avg_loss | -95.0015 |
| avg_hold_time_bars | 12.6052 |
| exposure | 0.1988 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
