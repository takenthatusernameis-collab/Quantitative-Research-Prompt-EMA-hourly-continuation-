# EMA Hourly Continuation — TAIKO/USDT P26_50

**Symbol:** TAIKO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.7077 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 1.0201 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -2.2734 |
| sortino_ratio | -0.6645 |
| max_drawdown | 0.5472 |
| cagr | -0.2618 |
| net_avg_win | 62.8557 |
| net_avg_loss | -90.6436 |
| avg_hold_time_bars | 7.0867 |
| exposure | 0.1334 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
