# EMA Hourly Continuation — SUSHI/USDT P50_144

**Symbol:** SUSHI/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.5575 |
| net_win_rate | 0.4575 |
| gross_profit_factor | 0.8287 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -3.9310 |
| sortino_ratio | -1.2618 |
| max_drawdown | 0.7938 |
| cagr | -0.4494 |
| net_avg_win | 41.3614 |
| net_avg_loss | -62.5733 |
| avg_hold_time_bars | 11.9517 |
| exposure | 0.2801 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
