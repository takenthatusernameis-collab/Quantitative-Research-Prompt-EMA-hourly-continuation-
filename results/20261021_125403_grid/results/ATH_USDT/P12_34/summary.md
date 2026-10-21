# EMA Hourly Continuation — ATH/USDT P12_34

**Symbol:** ATH/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.8622 |
| net_win_rate | 0.5268 |
| gross_profit_factor | 1.1107 |
| gross_win_rate | 0.5268 |
| sharpe_ratio | -1.0615 |
| sortino_ratio | -0.3546 |
| max_drawdown | 0.3726 |
| cagr | -0.1530 |
| net_avg_win | 76.4364 |
| net_avg_loss | -98.7102 |
| avg_hold_time_bars | 6.4076 |
| exposure | 0.1562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
