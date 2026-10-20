# EMA Hourly Continuation — BOME/USDT P20_34

**Symbol:** BOME/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1119 |
| net_profit_factor | 0.3814 |
| net_win_rate | 0.4254 |
| gross_profit_factor | 0.7392 |
| gross_win_rate | 0.4361 |
| sharpe_ratio | -9.1001 |
| sortino_ratio | -4.2909 |
| max_drawdown | 0.9956 |
| cagr | -0.8819 |
| net_avg_win | 12.8924 |
| net_avg_loss | -25.0233 |
| avg_hold_time_bars | 2.6309 |
| exposure | 0.1338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
