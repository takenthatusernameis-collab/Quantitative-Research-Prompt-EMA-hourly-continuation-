# EMA Hourly Continuation — IOTA/USDT P12_20

**Symbol:** IOTA/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.7827 |
| net_win_rate | 0.5356 |
| gross_profit_factor | 1.1508 |
| gross_win_rate | 0.5356 |
| sharpe_ratio | -1.5080 |
| sortino_ratio | -0.4252 |
| max_drawdown | 0.4246 |
| cagr | -0.1761 |
| net_avg_win | 68.3547 |
| net_avg_loss | -100.7275 |
| avg_hold_time_bars | 4.6148 |
| exposure | 0.0795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
