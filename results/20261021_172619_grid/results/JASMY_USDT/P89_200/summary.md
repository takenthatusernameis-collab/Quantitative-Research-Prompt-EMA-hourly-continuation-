# EMA Hourly Continuation — JASMY/USDT P89_200

**Symbol:** JASMY/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 1.0923 |
| net_win_rate | 0.5748 |
| gross_profit_factor | 1.3464 |
| gross_win_rate | 0.5748 |
| sharpe_ratio | 0.4774 |
| sortino_ratio | 0.1115 |
| max_drawdown | 0.1531 |
| cagr | 0.0437 |
| net_avg_win | 91.8807 |
| net_avg_loss | -113.7156 |
| avg_hold_time_bars | 17.4291 |
| exposure | 0.2012 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
