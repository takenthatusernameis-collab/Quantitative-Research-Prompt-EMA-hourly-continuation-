# EMA Hourly Continuation — ORCA/USDT P12_26

**Symbol:** ORCA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 602 |
| net_profit_factor | 0.7522 |
| net_win_rate | 0.5266 |
| gross_profit_factor | 1.1041 |
| gross_win_rate | 0.5299 |
| sharpe_ratio | -2.1935 |
| sortino_ratio | -0.7725 |
| max_drawdown | 0.6459 |
| cagr | -0.3003 |
| net_avg_win | 56.7147 |
| net_avg_loss | -83.8607 |
| avg_hold_time_bars | 5.9070 |
| exposure | 0.1616 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
