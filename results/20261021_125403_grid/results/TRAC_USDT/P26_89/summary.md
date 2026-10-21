# EMA Hourly Continuation — TRAC/USDT P26_89

**Symbol:** TRAC/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.8364 |
| net_win_rate | 0.5135 |
| gross_profit_factor | 1.0538 |
| gross_win_rate | 0.5135 |
| sharpe_ratio | -1.1723 |
| sortino_ratio | -0.3557 |
| max_drawdown | 0.4275 |
| cagr | -0.1526 |
| net_avg_win | 75.9734 |
| net_avg_loss | -95.8523 |
| avg_hold_time_bars | 13.8251 |
| exposure | 0.2803 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
