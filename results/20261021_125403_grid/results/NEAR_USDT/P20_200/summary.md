# EMA Hourly Continuation — NEAR/USDT P20_200

**Symbol:** NEAR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.9161 |
| net_win_rate | 0.5152 |
| gross_profit_factor | 1.0595 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -0.4427 |
| sortino_ratio | -0.1097 |
| max_drawdown | 0.2405 |
| cagr | -0.0526 |
| net_avg_win | 90.5941 |
| net_avg_loss | -105.0750 |
| avg_hold_time_bars | 46.2525 |
| exposure | 0.6244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
