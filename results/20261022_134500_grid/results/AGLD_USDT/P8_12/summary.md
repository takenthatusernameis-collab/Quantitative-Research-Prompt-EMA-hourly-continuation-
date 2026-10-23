# EMA Hourly Continuation — AGLD/USDT P8_12

**Symbol:** AGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1611 |
| net_profit_factor | 0.2459 |
| net_win_rate | 0.3917 |
| gross_profit_factor | 0.6870 |
| gross_win_rate | 0.4389 |
| sharpe_ratio | -13.8883 |
| sortino_ratio | -7.9342 |
| max_drawdown | 1.0000 |
| cagr | -0.9821 |
| net_avg_win | 5.1669 |
| net_avg_loss | -13.5305 |
| avg_hold_time_bars | 2.7374 |
| exposure | 0.1996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
