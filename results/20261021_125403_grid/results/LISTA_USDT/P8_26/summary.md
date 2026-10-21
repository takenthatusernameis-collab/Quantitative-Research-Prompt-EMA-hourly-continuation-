# EMA Hourly Continuation — LISTA/USDT P8_26

**Symbol:** LISTA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 728 |
| net_profit_factor | 0.7509 |
| net_win_rate | 0.4863 |
| gross_profit_factor | 0.9750 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -2.9324 |
| sortino_ratio | -1.1723 |
| max_drawdown | 0.7456 |
| cagr | -0.4162 |
| net_avg_win | 60.8935 |
| net_avg_loss | -76.7622 |
| avg_hold_time_bars | 6.7940 |
| exposure | 0.2418 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
