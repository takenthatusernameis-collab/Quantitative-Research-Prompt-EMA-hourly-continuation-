# EMA Hourly Continuation — TRAC/USDT P34_89

**Symbol:** TRAC/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.5506 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 0.9063 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -4.5311 |
| sortino_ratio | -1.6147 |
| max_drawdown | 0.8658 |
| cagr | -0.5445 |
| net_avg_win | 34.9411 |
| net_avg_loss | -55.0707 |
| avg_hold_time_bars | 8.0154 |
| exposure | 0.2368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
