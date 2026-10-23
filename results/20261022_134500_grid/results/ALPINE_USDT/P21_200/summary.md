# EMA Hourly Continuation — ALPINE/USDT P21_200

**Symbol:** ALPINE/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.8334 |
| net_win_rate | 0.5242 |
| gross_profit_factor | 1.0876 |
| gross_win_rate | 0.5242 |
| sharpe_ratio | -0.8011 |
| sortino_ratio | -0.1721 |
| max_drawdown | 0.2210 |
| cagr | -0.0782 |
| net_avg_win | 77.7218 |
| net_avg_loss | -102.7545 |
| avg_hold_time_bars | 75.8811 |
| exposure | 0.7830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
