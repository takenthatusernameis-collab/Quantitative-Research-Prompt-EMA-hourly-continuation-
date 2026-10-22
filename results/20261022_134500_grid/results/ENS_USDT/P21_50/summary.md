# EMA Hourly Continuation — ENS/USDT P21_50

**Symbol:** ENS/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1022 |
| net_profit_factor | 0.5296 |
| net_win_rate | 0.4325 |
| gross_profit_factor | 0.8864 |
| gross_win_rate | 0.4452 |
| sharpe_ratio | -8.2369 |
| sortino_ratio | -3.7025 |
| max_drawdown | 0.9912 |
| cagr | -0.8421 |
| net_avg_win | 25.2279 |
| net_avg_loss | -36.2994 |
| avg_hold_time_bars | 4.8885 |
| exposure | 0.2271 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
