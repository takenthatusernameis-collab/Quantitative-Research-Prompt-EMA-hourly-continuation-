# EMA Hourly Continuation — EGLD/USDT P12_100

**Symbol:** EGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.8405 |
| net_win_rate | 0.5122 |
| gross_profit_factor | 1.0471 |
| gross_win_rate | 0.5122 |
| sharpe_ratio | -1.1618 |
| sortino_ratio | -0.3543 |
| max_drawdown | 0.4443 |
| cagr | -0.1524 |
| net_avg_win | 77.5430 |
| net_avg_loss | -96.8670 |
| avg_hold_time_bars | 29.6763 |
| exposure | 0.6084 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
