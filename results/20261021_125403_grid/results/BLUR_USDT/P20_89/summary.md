# EMA Hourly Continuation — BLUR/USDT P20_89

**Symbol:** BLUR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.8381 |
| net_win_rate | 0.5099 |
| gross_profit_factor | 1.0498 |
| gross_win_rate | 0.5099 |
| sharpe_ratio | -1.3715 |
| sortino_ratio | -0.4414 |
| max_drawdown | 0.5186 |
| cagr | -0.1857 |
| net_avg_win | 81.1570 |
| net_avg_loss | -100.7355 |
| avg_hold_time_bars | 17.1957 |
| exposure | 0.3937 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
