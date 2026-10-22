# EMA Hourly Continuation — FLIP/USDT P100_200

**Symbol:** FLIP/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 207 |
| net_profit_factor | 0.4834 |
| net_win_rate | 0.4106 |
| gross_profit_factor | 0.6798 |
| gross_win_rate | 0.4155 |
| sharpe_ratio | -3.0540 |
| sortino_ratio | -0.6208 |
| max_drawdown | 0.5288 |
| cagr | -0.2489 |
| net_avg_win | 56.4261 |
| net_avg_loss | -81.3300 |
| avg_hold_time_bars | 21.3671 |
| exposure | 0.2010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
