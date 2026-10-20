# EMA Hourly Continuation — BRETT/USDT P12_100

**Symbol:** BRETT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 618 |
| net_profit_factor | 0.7385 |
| net_win_rate | 0.4871 |
| gross_profit_factor | 0.9754 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -2.6308 |
| sortino_ratio | -0.9480 |
| max_drawdown | 0.6626 |
| cagr | -0.3637 |
| net_avg_win | 61.7203 |
| net_avg_loss | -79.3579 |
| avg_hold_time_bars | 19.3382 |
| exposure | 0.5750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
