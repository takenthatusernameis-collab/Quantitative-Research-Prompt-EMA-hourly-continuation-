# EMA Hourly Continuation — FLOKI/USDT P12_50

**Symbol:** FLOKI/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1129 |
| net_profit_factor | 0.5613 |
| net_win_rate | 0.4562 |
| gross_profit_factor | 0.8541 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -6.8282 |
| sortino_ratio | -3.2257 |
| max_drawdown | 0.9805 |
| cagr | -0.7906 |
| net_avg_win | 24.3592 |
| net_avg_loss | -36.3973 |
| avg_hold_time_bars | 6.9539 |
| exposure | 0.3569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
