# EMA Hourly Continuation — CELO/USDT P55_200

**Symbol:** CELO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.9364 |
| net_win_rate | 0.5362 |
| gross_profit_factor | 1.1595 |
| gross_win_rate | 0.5362 |
| sharpe_ratio | -0.3418 |
| sortino_ratio | -0.0859 |
| max_drawdown | 0.2575 |
| cagr | -0.0426 |
| net_avg_win | 93.9254 |
| net_avg_loss | -115.9567 |
| avg_hold_time_bars | 24.0197 |
| exposure | 0.3304 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
