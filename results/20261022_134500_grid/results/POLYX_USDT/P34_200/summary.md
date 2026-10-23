# EMA Hourly Continuation — POLYX/USDT P34_200

**Symbol:** POLYX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.6884 |
| net_win_rate | 0.4809 |
| gross_profit_factor | 0.9776 |
| gross_win_rate | 0.4962 |
| sharpe_ratio | -2.3120 |
| sortino_ratio | -0.6498 |
| max_drawdown | 0.5634 |
| cagr | -0.2618 |
| net_avg_win | 62.3627 |
| net_avg_loss | -83.9261 |
| avg_hold_time_bars | 27.6081 |
| exposure | 0.4932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
