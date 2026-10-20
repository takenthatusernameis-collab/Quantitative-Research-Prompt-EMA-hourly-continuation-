# EMA Hourly Continuation — SATS/USDT P144_200

**Symbol:** SATS/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.4033 |
| net_win_rate | 0.3881 |
| gross_profit_factor | 0.6480 |
| gross_win_rate | 0.3935 |
| sharpe_ratio | -5.1013 |
| sortino_ratio | -1.3830 |
| max_drawdown | 0.8157 |
| cagr | -0.4873 |
| net_avg_win | 38.2294 |
| net_avg_loss | -60.1360 |
| avg_hold_time_bars | 5.6065 |
| exposure | 0.0941 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
