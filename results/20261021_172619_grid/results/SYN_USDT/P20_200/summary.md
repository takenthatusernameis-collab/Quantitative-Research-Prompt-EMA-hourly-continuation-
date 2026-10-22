# EMA Hourly Continuation — SYN/USDT P20_200

**Symbol:** SYN/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.9918 |
| net_win_rate | 0.5370 |
| gross_profit_factor | 1.1534 |
| gross_win_rate | 0.5370 |
| sharpe_ratio | 0.0118 |
| sortino_ratio | 0.0030 |
| max_drawdown | 0.1875 |
| cagr | -0.0049 |
| net_avg_win | 88.4499 |
| net_avg_loss | -103.4249 |
| avg_hold_time_bars | 45.4309 |
| exposure | 0.6422 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
