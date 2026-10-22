# EMA Hourly Continuation — EIGEN/USDT P20_21

**Symbol:** EIGEN/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 993 |
| net_profit_factor | 0.2288 |
| net_win_rate | 0.3353 |
| gross_profit_factor | 0.5751 |
| gross_win_rate | 0.3736 |
| sharpe_ratio | -15.7773 |
| sortino_ratio | -8.0180 |
| max_drawdown | 0.9999 |
| cagr | -0.9894 |
| net_avg_win | 8.9087 |
| net_avg_loss | -19.6450 |
| avg_hold_time_bars | 1.6657 |
| exposure | 0.0920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
