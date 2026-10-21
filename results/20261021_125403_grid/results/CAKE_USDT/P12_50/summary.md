# EMA Hourly Continuation — CAKE/USDT P12_50

**Symbol:** CAKE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 582 |
| net_profit_factor | 0.7727 |
| net_win_rate | 0.5069 |
| gross_profit_factor | 1.0456 |
| gross_win_rate | 0.5069 |
| sharpe_ratio | -2.1271 |
| sortino_ratio | -0.7366 |
| max_drawdown | 0.5987 |
| cagr | -0.2875 |
| net_avg_win | 66.0618 |
| net_avg_loss | -87.8728 |
| avg_hold_time_bars | 13.3557 |
| exposure | 0.3533 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
