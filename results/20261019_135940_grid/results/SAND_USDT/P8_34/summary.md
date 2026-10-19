# EMA Hourly Continuation — SAND/USDT P8_34

**Symbol:** SAND/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1316 |
| net_profit_factor | 0.3937 |
| net_win_rate | 0.4392 |
| gross_profit_factor | 0.7812 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -8.8959 |
| sortino_ratio | -4.5294 |
| max_drawdown | 0.9965 |
| cagr | -0.8936 |
| net_avg_win | 11.1931 |
| net_avg_loss | -22.2678 |
| avg_hold_time_bars | 5.8913 |
| exposure | 0.3524 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
