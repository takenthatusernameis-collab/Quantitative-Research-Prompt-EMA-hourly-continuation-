# EMA Hourly Continuation — ELON/USDT P55_100

**Symbol:** ELON/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.4034 |
| net_win_rate | 0.4413 |
| gross_profit_factor | 0.7323 |
| gross_win_rate | 0.4430 |
| sharpe_ratio | -6.0130 |
| sortino_ratio | -2.0925 |
| max_drawdown | 0.9218 |
| cagr | -0.6323 |
| net_avg_win | 23.6259 |
| net_avg_loss | -46.2550 |
| avg_hold_time_bars | 4.9849 |
| exposure | 0.1350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
