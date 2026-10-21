# EMA Hourly Continuation — METIS/USDT P12_21

**Symbol:** METIS/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.6569 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9289 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -2.6485 |
| sortino_ratio | -0.7489 |
| max_drawdown | 0.5970 |
| cagr | -0.2912 |
| net_avg_win | 58.9320 |
| net_avg_loss | -83.4911 |
| avg_hold_time_bars | 4.9128 |
| exposure | 0.0871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
