# EMA Hourly Continuation — ALPINE/USDT P21_34

**Symbol:** ALPINE/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1016 |
| net_profit_factor | 0.3303 |
| net_win_rate | 0.3720 |
| gross_profit_factor | 0.6833 |
| gross_win_rate | 0.4134 |
| sharpe_ratio | -11.2836 |
| sortino_ratio | -5.1329 |
| max_drawdown | 0.9985 |
| cagr | -0.9253 |
| net_avg_win | 13.0290 |
| net_avg_loss | -23.3702 |
| avg_hold_time_bars | 4.1427 |
| exposure | 0.1913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
