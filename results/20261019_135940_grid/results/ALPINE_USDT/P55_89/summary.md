# EMA Hourly Continuation — ALPINE/USDT P55_89

**Symbol:** ALPINE/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 647 |
| net_profit_factor | 0.4451 |
| net_win_rate | 0.4204 |
| gross_profit_factor | 0.8737 |
| gross_win_rate | 0.4498 |
| sharpe_ratio | -7.0943 |
| sortino_ratio | -2.5429 |
| max_drawdown | 0.9587 |
| cagr | -0.7176 |
| net_avg_win | 28.2611 |
| net_avg_loss | -46.0514 |
| avg_hold_time_bars | 5.6121 |
| exposure | 0.1650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
