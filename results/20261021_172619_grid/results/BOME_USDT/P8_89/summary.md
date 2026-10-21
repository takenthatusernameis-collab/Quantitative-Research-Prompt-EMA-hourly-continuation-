# EMA Hourly Continuation — BOME/USDT P8_89

**Symbol:** BOME/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.8588 |
| net_win_rate | 0.5067 |
| gross_profit_factor | 1.0051 |
| gross_win_rate | 0.5067 |
| sharpe_ratio | -0.9734 |
| sortino_ratio | -0.3195 |
| max_drawdown | 0.4209 |
| cagr | -0.1405 |
| net_avg_win | 72.3411 |
| net_avg_loss | -86.5119 |
| avg_hold_time_bars | 25.2876 |
| exposure | 0.6035 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
