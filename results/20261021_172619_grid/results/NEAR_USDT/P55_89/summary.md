# EMA Hourly Continuation — NEAR/USDT P55_89

**Symbol:** NEAR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.7081 |
| net_win_rate | 0.4877 |
| gross_profit_factor | 0.9321 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -1.5759 |
| sortino_ratio | -0.3524 |
| max_drawdown | 0.3445 |
| cagr | -0.1486 |
| net_avg_win | 67.7223 |
| net_avg_loss | -91.0544 |
| avg_hold_time_bars | 5.5820 |
| exposure | 0.0619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
