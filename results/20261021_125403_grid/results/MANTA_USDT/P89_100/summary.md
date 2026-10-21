# EMA Hourly Continuation — MANTA/USDT P89_100

**Symbol:** MANTA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 136 |
| net_profit_factor | 0.5556 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.8143 |
| gross_win_rate | 0.4412 |
| sharpe_ratio | -2.2504 |
| sortino_ratio | -0.3755 |
| max_drawdown | 0.3718 |
| cagr | -0.1593 |
| net_avg_win | 73.5888 |
| net_avg_loss | -104.5729 |
| avg_hold_time_bars | 5.4044 |
| exposure | 0.0334 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
