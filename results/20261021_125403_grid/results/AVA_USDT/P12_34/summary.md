# EMA Hourly Continuation — AVA/USDT P12_34

**Symbol:** AVA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 600 |
| net_profit_factor | 0.6566 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.9006 |
| gross_win_rate | 0.4750 |
| sharpe_ratio | -3.2813 |
| sortino_ratio | -1.1496 |
| max_drawdown | 0.7526 |
| cagr | -0.4096 |
| net_avg_win | 49.2273 |
| net_avg_loss | -67.8340 |
| avg_hold_time_bars | 6.4683 |
| exposure | 0.1764 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
