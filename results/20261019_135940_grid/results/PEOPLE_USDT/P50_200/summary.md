# EMA Hourly Continuation — PEOPLE/USDT P50_200

**Symbol:** PEOPLE/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.7550 |
| net_win_rate | 0.4974 |
| gross_profit_factor | 0.9871 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -1.6413 |
| sortino_ratio | -0.4515 |
| max_drawdown | 0.4827 |
| cagr | -0.1913 |
| net_avg_win | 67.9741 |
| net_avg_loss | -89.0848 |
| avg_hold_time_bars | 23.0820 |
| exposure | 0.3948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
