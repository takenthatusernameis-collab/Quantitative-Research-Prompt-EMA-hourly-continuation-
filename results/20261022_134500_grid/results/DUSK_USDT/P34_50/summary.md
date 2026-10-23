# EMA Hourly Continuation — DUSK/USDT P34_50

**Symbol:** DUSK/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 881 |
| net_profit_factor | 0.4478 |
| net_win_rate | 0.4234 |
| gross_profit_factor | 0.8984 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -8.1092 |
| sortino_ratio | -3.3837 |
| max_drawdown | 0.9868 |
| cagr | -0.8168 |
| net_avg_win | 21.4318 |
| net_avg_loss | -35.1438 |
| avg_hold_time_bars | 3.0636 |
| exposure | 0.1227 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
