# EMA Hourly Continuation — MOCA/USDT P50_89

**Symbol:** MOCA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.7703 |
| net_win_rate | 0.5106 |
| gross_profit_factor | 1.0367 |
| gross_win_rate | 0.5106 |
| sharpe_ratio | -1.5713 |
| sortino_ratio | -0.4302 |
| max_drawdown | 0.4051 |
| cagr | -0.1792 |
| net_avg_win | 72.2942 |
| net_avg_loss | -97.9299 |
| avg_hold_time_bars | 7.1854 |
| exposure | 0.1185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
