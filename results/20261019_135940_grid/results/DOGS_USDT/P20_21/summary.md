# EMA Hourly Continuation — DOGS/USDT P20_21

**Symbol:** DOGS/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1105 |
| net_profit_factor | 0.1433 |
| net_win_rate | 0.2968 |
| gross_profit_factor | 0.4250 |
| gross_win_rate | 0.3439 |
| sharpe_ratio | -18.2172 |
| sortino_ratio | -9.8398 |
| max_drawdown | 1.0000 |
| cagr | -0.9960 |
| net_avg_win | 5.0982 |
| net_avg_loss | -15.0221 |
| avg_hold_time_bars | 1.4914 |
| exposure | 0.0874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
