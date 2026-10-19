# EMA Hourly Continuation — PENDLE/USDT P34_89

**Symbol:** PENDLE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 742 |
| net_profit_factor | 0.5719 |
| net_win_rate | 0.4650 |
| gross_profit_factor | 0.8665 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -4.8575 |
| sortino_ratio | -1.8533 |
| max_drawdown | 0.8959 |
| cagr | -0.5937 |
| net_avg_win | 34.6949 |
| net_avg_loss | -52.7155 |
| avg_hold_time_bars | 6.7561 |
| exposure | 0.2279 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
