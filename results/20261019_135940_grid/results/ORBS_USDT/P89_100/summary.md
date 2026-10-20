# EMA Hourly Continuation — ORBS/USDT P89_100

**Symbol:** ORBS/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.1940 |
| net_win_rate | 0.3329 |
| gross_profit_factor | 0.6851 |
| gross_win_rate | 0.3989 |
| sharpe_ratio | -11.8817 |
| sortino_ratio | -4.6523 |
| max_drawdown | 0.9980 |
| cagr | -0.9150 |
| net_avg_win | 10.3511 |
| net_avg_loss | -26.6257 |
| avg_hold_time_bars | 2.8895 |
| exposure | 0.0915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
