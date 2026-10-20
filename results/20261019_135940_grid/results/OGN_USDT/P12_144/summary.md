# EMA Hourly Continuation — OGN/USDT P12_144

**Symbol:** OGN/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.5632 |
| net_win_rate | 0.4391 |
| gross_profit_factor | 0.8423 |
| gross_win_rate | 0.4517 |
| sharpe_ratio | -4.1734 |
| sortino_ratio | -1.2695 |
| max_drawdown | 0.8020 |
| cagr | -0.4601 |
| net_avg_win | 48.6628 |
| net_avg_loss | -67.6328 |
| avg_hold_time_bars | 31.8424 |
| exposure | 0.6859 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
