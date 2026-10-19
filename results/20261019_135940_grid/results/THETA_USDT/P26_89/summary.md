# EMA Hourly Continuation — THETA/USDT P26_89

**Symbol:** THETA/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 711 |
| net_profit_factor | 0.5968 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 0.9423 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -4.4663 |
| sortino_ratio | -1.6813 |
| max_drawdown | 0.8737 |
| cagr | -0.5504 |
| net_avg_win | 38.2542 |
| net_avg_loss | -57.1059 |
| avg_hold_time_bars | 8.9930 |
| exposure | 0.2906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
