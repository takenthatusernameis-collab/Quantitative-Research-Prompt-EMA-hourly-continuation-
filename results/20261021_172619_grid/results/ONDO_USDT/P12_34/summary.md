# EMA Hourly Continuation — ONDO/USDT P12_34

**Symbol:** ONDO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.8331 |
| net_win_rate | 0.5162 |
| gross_profit_factor | 1.0724 |
| gross_win_rate | 0.5162 |
| sharpe_ratio | -1.3757 |
| sortino_ratio | -0.4537 |
| max_drawdown | 0.4844 |
| cagr | -0.1894 |
| net_avg_win | 75.4746 |
| net_avg_loss | -96.6603 |
| avg_hold_time_bars | 7.2248 |
| exposure | 0.1724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
