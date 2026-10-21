# EMA Hourly Continuation — NEAR/USDT P20_55

**Symbol:** NEAR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.7443 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9363 |
| gross_win_rate | 0.4834 |
| sharpe_ratio | -2.0132 |
| sortino_ratio | -0.6106 |
| max_drawdown | 0.5303 |
| cagr | -0.2456 |
| net_avg_win | 67.7548 |
| net_avg_loss | -85.1665 |
| avg_hold_time_bars | 9.2506 |
| exposure | 0.1896 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
