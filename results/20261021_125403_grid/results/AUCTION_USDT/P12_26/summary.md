# EMA Hourly Continuation — AUCTION/USDT P12_26

**Symbol:** AUCTION/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.5275 |
| net_win_rate | 0.4313 |
| gross_profit_factor | 0.7787 |
| gross_win_rate | 0.4329 |
| sharpe_ratio | -5.5400 |
| sortino_ratio | -1.9835 |
| max_drawdown | 0.9069 |
| cagr | -0.6046 |
| net_avg_win | 36.9622 |
| net_avg_loss | -53.1323 |
| avg_hold_time_bars | 6.1453 |
| exposure | 0.1761 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
