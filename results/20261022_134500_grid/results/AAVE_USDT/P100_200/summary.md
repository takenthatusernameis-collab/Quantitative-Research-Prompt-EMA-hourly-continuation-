# EMA Hourly Continuation — AAVE/USDT P100_200

**Symbol:** AAVE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.5076 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.8050 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -3.8207 |
| sortino_ratio | -1.0578 |
| max_drawdown | 0.7268 |
| cagr | -0.4012 |
| net_avg_win | 42.6586 |
| net_avg_loss | -69.0454 |
| avg_hold_time_bars | 9.1263 |
| exposure | 0.1610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
