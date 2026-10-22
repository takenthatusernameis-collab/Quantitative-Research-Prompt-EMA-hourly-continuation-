# EMA Hourly Continuation — AIOZ/USDT P12_26

**Symbol:** AIOZ/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1486 |
| net_profit_factor | 0.4760 |
| net_win_rate | 0.4085 |
| gross_profit_factor | 0.8508 |
| gross_win_rate | 0.4273 |
| sharpe_ratio | -11.4378 |
| sortino_ratio | -6.1755 |
| max_drawdown | 0.9996 |
| cagr | -0.9564 |
| net_avg_win | 14.9602 |
| net_avg_loss | -21.7031 |
| avg_hold_time_bars | 2.8755 |
| exposure | 0.1942 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
