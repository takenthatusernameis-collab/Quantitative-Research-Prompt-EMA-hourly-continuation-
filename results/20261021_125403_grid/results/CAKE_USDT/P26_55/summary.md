# EMA Hourly Continuation — CAKE/USDT P26_55

**Symbol:** CAKE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.6746 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9818 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -2.7020 |
| sortino_ratio | -0.8180 |
| max_drawdown | 0.6107 |
| cagr | -0.3132 |
| net_avg_win | 57.8123 |
| net_avg_loss | -83.0455 |
| avg_hold_time_bars | 8.0764 |
| exposure | 0.1634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
