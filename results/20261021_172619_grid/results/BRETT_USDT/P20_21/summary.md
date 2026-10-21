# EMA Hourly Continuation — BRETT/USDT P20_21

**Symbol:** BRETT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 120 |
| net_profit_factor | 0.9178 |
| net_win_rate | 0.5417 |
| gross_profit_factor | 1.1760 |
| gross_win_rate | 0.5417 |
| sharpe_ratio | -0.2906 |
| sortino_ratio | -0.0474 |
| max_drawdown | 0.1674 |
| cagr | -0.0230 |
| net_avg_win | 92.2994 |
| net_avg_loss | -118.8552 |
| avg_hold_time_bars | 5.1750 |
| exposure | 0.0299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
