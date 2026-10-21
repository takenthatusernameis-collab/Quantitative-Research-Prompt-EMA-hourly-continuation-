# EMA Hourly Continuation — 1INCH/USDT P12_26

**Symbol:** 1INCH/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.5861 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.8607 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -3.7188 |
| sortino_ratio | -1.2083 |
| max_drawdown | 0.7533 |
| cagr | -0.4252 |
| net_avg_win | 43.9404 |
| net_avg_loss | -66.7068 |
| avg_hold_time_bars | 5.6732 |
| exposure | 0.1325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
