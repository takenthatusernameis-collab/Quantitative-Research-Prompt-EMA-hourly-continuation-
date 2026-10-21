# EMA Hourly Continuation — SUSHI/USDT P34_50

**Symbol:** SUSHI/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.6822 |
| net_win_rate | 0.4910 |
| gross_profit_factor | 0.9658 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -2.0058 |
| sortino_ratio | -0.4796 |
| max_drawdown | 0.4244 |
| cagr | -0.1965 |
| net_avg_win | 66.4755 |
| net_avg_loss | -94.0093 |
| avg_hold_time_bars | 5.6057 |
| exposure | 0.0708 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
