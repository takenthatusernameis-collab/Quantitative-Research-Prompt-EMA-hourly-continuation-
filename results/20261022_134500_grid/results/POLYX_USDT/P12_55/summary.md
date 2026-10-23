# EMA Hourly Continuation — POLYX/USDT P12_55

**Symbol:** POLYX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 952 |
| net_profit_factor | 0.6013 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9508 |
| gross_win_rate | 0.4916 |
| sharpe_ratio | -5.2418 |
| sortino_ratio | -2.2711 |
| max_drawdown | 0.9374 |
| cagr | -0.6658 |
| net_avg_win | 30.9587 |
| net_avg_loss | -47.3371 |
| avg_hold_time_bars | 8.8445 |
| exposure | 0.3827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
