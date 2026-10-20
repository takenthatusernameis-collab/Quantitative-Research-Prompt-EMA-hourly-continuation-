# EMA Hourly Continuation — DEEP/USDT P26_144

**Symbol:** DEEP/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.7776 |
| net_win_rate | 0.5047 |
| gross_profit_factor | 0.9938 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -1.4764 |
| sortino_ratio | -0.4172 |
| max_drawdown | 0.3567 |
| cagr | -0.1805 |
| net_avg_win | 71.3212 |
| net_avg_loss | -93.4559 |
| avg_hold_time_bars | 29.4766 |
| exposure | 0.5357 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
