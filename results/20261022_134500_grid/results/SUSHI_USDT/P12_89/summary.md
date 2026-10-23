# EMA Hourly Continuation — SUSHI/USDT P12_89

**Symbol:** SUSHI/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.5594 |
| net_win_rate | 0.4320 |
| gross_profit_factor | 0.8200 |
| gross_win_rate | 0.4381 |
| sharpe_ratio | -5.1942 |
| sortino_ratio | -1.8683 |
| max_drawdown | 0.9003 |
| cagr | -0.5953 |
| net_avg_win | 39.8666 |
| net_avg_loss | -54.2041 |
| avg_hold_time_bars | 18.7372 |
| exposure | 0.5613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
