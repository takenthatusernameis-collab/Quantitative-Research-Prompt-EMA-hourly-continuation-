# EMA Hourly Continuation — LSK/USDT P26_89

**Symbol:** LSK/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.7216 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 0.9781 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -2.3465 |
| sortino_ratio | -0.7583 |
| max_drawdown | 0.6132 |
| cagr | -0.2951 |
| net_avg_win | 60.1110 |
| net_avg_loss | -81.0523 |
| avg_hold_time_bars | 13.0039 |
| exposure | 0.3020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
