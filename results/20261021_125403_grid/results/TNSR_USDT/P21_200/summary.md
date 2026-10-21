# EMA Hourly Continuation — TNSR/USDT P21_200

**Symbol:** TNSR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.7484 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 0.8881 |
| gross_win_rate | 0.4704 |
| sharpe_ratio | -1.7160 |
| sortino_ratio | -0.4472 |
| max_drawdown | 0.4409 |
| cagr | -0.1868 |
| net_avg_win | 76.0174 |
| net_avg_loss | -90.2268 |
| avg_hold_time_bars | 39.8166 |
| exposure | 0.6090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
