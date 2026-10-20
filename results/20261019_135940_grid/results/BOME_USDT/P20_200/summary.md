# EMA Hourly Continuation — BOME/USDT P20_200

**Symbol:** BOME/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.6884 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9189 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -2.1011 |
| sortino_ratio | -0.5524 |
| max_drawdown | 0.5187 |
| cagr | -0.2328 |
| net_avg_win | 62.7657 |
| net_avg_loss | -85.2036 |
| avg_hold_time_bars | 40.7938 |
| exposure | 0.6564 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
