# EMA Hourly Continuation — AAVE/USDT P55_100

**Symbol:** AAVE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.8451 |
| net_win_rate | 0.5263 |
| gross_profit_factor | 1.1103 |
| gross_win_rate | 0.5263 |
| sharpe_ratio | -0.9532 |
| sortino_ratio | -0.2472 |
| max_drawdown | 0.3500 |
| cagr | -0.1086 |
| net_avg_win | 80.5237 |
| net_avg_loss | -105.8664 |
| avg_hold_time_bars | 8.0805 |
| exposure | 0.1186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
