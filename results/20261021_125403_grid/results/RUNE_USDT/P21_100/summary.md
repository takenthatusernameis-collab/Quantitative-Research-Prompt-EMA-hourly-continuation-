# EMA Hourly Continuation — RUNE/USDT P21_100

**Symbol:** RUNE/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.8470 |
| net_win_rate | 0.5193 |
| gross_profit_factor | 1.0676 |
| gross_win_rate | 0.5193 |
| sharpe_ratio | -0.9566 |
| sortino_ratio | -0.2618 |
| max_drawdown | 0.3243 |
| cagr | -0.1153 |
| net_avg_win | 78.0219 |
| net_avg_loss | -99.5218 |
| avg_hold_time_bars | 31.6989 |
| exposure | 0.5216 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
