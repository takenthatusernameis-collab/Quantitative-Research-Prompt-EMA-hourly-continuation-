# EMA Hourly Continuation — LUNA/USDT P21_100

**Symbol:** LUNA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 787 |
| net_profit_factor | 0.5097 |
| net_win_rate | 0.4333 |
| gross_profit_factor | 0.8824 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -6.8848 |
| sortino_ratio | -2.7052 |
| max_drawdown | 0.9673 |
| cagr | -0.7428 |
| net_avg_win | 29.4775 |
| net_avg_loss | -44.2183 |
| avg_hold_time_bars | 10.2618 |
| exposure | 0.3671 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
