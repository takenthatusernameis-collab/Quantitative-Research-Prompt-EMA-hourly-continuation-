# EMA Hourly Continuation — THETA/USDT P8_34

**Symbol:** THETA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 745 |
| net_profit_factor | 0.7643 |
| net_win_rate | 0.4953 |
| gross_profit_factor | 0.9852 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -2.4046 |
| sortino_ratio | -0.9404 |
| max_drawdown | 0.6725 |
| cagr | -0.3509 |
| net_avg_win | 58.1746 |
| net_avg_loss | -74.7026 |
| avg_hold_time_bars | 8.1289 |
| exposure | 0.2753 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
