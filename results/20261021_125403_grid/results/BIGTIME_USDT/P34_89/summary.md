# EMA Hourly Continuation — BIGTIME/USDT P34_89

**Symbol:** BIGTIME/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.8067 |
| net_win_rate | 0.5086 |
| gross_profit_factor | 1.0346 |
| gross_win_rate | 0.5086 |
| sharpe_ratio | -1.4902 |
| sortino_ratio | -0.4596 |
| max_drawdown | 0.4780 |
| cagr | -0.1915 |
| net_avg_win | 73.4138 |
| net_avg_loss | -94.1954 |
| avg_hold_time_bars | 11.5776 |
| exposure | 0.2431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
