# EMA Hourly Continuation — GRAM/USDT P34_89

**Symbol:** GRAM/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 758 |
| net_profit_factor | 0.3878 |
| net_win_rate | 0.4261 |
| gross_profit_factor | 0.8213 |
| gross_win_rate | 0.4446 |
| sharpe_ratio | -7.6310 |
| sortino_ratio | -2.9382 |
| max_drawdown | 0.9781 |
| cagr | -0.7751 |
| net_avg_win | 19.1500 |
| net_avg_loss | -36.6657 |
| avg_hold_time_bars | 6.8430 |
| exposure | 0.2358 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
