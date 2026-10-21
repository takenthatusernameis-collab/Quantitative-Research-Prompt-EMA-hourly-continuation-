# EMA Hourly Continuation — CELO/USDT P55_100

**Symbol:** CELO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.9231 |
| net_win_rate | 0.5552 |
| gross_profit_factor | 1.2497 |
| gross_win_rate | 0.5552 |
| sharpe_ratio | -0.4321 |
| sortino_ratio | -0.1161 |
| max_drawdown | 0.2041 |
| cagr | -0.0556 |
| net_avg_win | 84.4992 |
| net_avg_loss | -114.2722 |
| avg_hold_time_bars | 8.7994 |
| exposure | 0.1370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
