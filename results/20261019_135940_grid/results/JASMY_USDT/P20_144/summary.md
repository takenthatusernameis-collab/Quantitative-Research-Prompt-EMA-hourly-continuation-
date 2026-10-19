# EMA Hourly Continuation — JASMY/USDT P20_144

**Symbol:** JASMY/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.8807 |
| net_win_rate | 0.5632 |
| gross_profit_factor | 1.2650 |
| gross_win_rate | 0.5632 |
| sharpe_ratio | -0.7628 |
| sortino_ratio | -0.2324 |
| max_drawdown | 0.3445 |
| cagr | -0.1111 |
| net_avg_win | 71.8759 |
| net_avg_loss | -105.2145 |
| avg_hold_time_bars | 26.6488 |
| exposure | 0.5657 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
