# EMA Hourly Continuation — FLOW/USDT P20_55

**Symbol:** FLOW/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 953 |
| net_profit_factor | 0.4628 |
| net_win_rate | 0.4334 |
| gross_profit_factor | 0.8610 |
| gross_win_rate | 0.4502 |
| sharpe_ratio | -7.6188 |
| sortino_ratio | -3.3126 |
| max_drawdown | 0.9838 |
| cagr | -0.8027 |
| net_avg_win | 20.5064 |
| net_avg_loss | -33.8879 |
| avg_hold_time_bars | 5.6590 |
| exposure | 0.2451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
