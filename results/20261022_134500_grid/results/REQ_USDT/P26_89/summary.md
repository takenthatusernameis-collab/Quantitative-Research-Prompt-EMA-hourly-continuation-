# EMA Hourly Continuation — REQ/USDT P26_89

**Symbol:** REQ/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 832 |
| net_profit_factor | 0.4694 |
| net_win_rate | 0.4255 |
| gross_profit_factor | 0.9084 |
| gross_win_rate | 0.4471 |
| sharpe_ratio | -8.2001 |
| sortino_ratio | -3.3405 |
| max_drawdown | 0.9859 |
| cagr | -0.8142 |
| net_avg_win | 24.6212 |
| net_avg_loss | -38.8493 |
| avg_hold_time_bars | 8.8125 |
| exposure | 0.3333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
