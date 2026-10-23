# EMA Hourly Continuation — ALEX/USDT P26_50

**Symbol:** ALEX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 806 |
| net_profit_factor | 0.4364 |
| net_win_rate | 0.3685 |
| gross_profit_factor | 0.8120 |
| gross_win_rate | 0.3945 |
| sharpe_ratio | -9.1270 |
| sortino_ratio | -3.6504 |
| max_drawdown | 0.9910 |
| cagr | -0.8424 |
| net_avg_win | 25.8170 |
| net_avg_loss | -34.5209 |
| avg_hold_time_bars | 5.8089 |
| exposure | 0.2128 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
