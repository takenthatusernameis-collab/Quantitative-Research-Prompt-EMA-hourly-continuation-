# EMA Hourly Continuation — ENA/USDT P8_34

**Symbol:** ENA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.8834 |
| net_win_rate | 0.5213 |
| gross_profit_factor | 1.0659 |
| gross_win_rate | 0.5213 |
| sharpe_ratio | -0.8659 |
| sortino_ratio | -0.3254 |
| max_drawdown | 0.4193 |
| cagr | -0.1448 |
| net_avg_win | 69.3209 |
| net_avg_loss | -85.4517 |
| avg_hold_time_bars | 8.8532 |
| exposure | 0.2740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
