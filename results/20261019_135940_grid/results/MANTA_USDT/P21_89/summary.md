# EMA Hourly Continuation — MANTA/USDT P21_89

**Symbol:** MANTA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 640 |
| net_profit_factor | 0.6818 |
| net_win_rate | 0.4875 |
| gross_profit_factor | 0.9926 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -3.4457 |
| sortino_ratio | -1.2217 |
| max_drawdown | 0.7733 |
| cagr | -0.4440 |
| net_avg_win | 52.9421 |
| net_avg_loss | -73.8668 |
| avg_hold_time_bars | 14.4391 |
| exposure | 0.4200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
