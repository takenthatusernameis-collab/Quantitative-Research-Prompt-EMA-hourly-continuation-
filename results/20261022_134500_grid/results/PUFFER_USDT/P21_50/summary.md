# EMA Hourly Continuation — PUFFER/USDT P21_50

**Symbol:** PUFFER/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 736 |
| net_profit_factor | 0.6253 |
| net_win_rate | 0.4905 |
| gross_profit_factor | 0.9876 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -4.5159 |
| sortino_ratio | -1.9292 |
| max_drawdown | 0.8480 |
| cagr | -0.6036 |
| net_avg_win | 39.0674 |
| net_avg_loss | -60.1502 |
| avg_hold_time_bars | 5.2201 |
| exposure | 0.2174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
