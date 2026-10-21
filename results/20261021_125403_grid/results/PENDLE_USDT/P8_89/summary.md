# EMA Hourly Continuation — PENDLE/USDT P8_89

**Symbol:** PENDLE/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.7995 |
| net_win_rate | 0.4865 |
| gross_profit_factor | 0.9384 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -1.4985 |
| sortino_ratio | -0.4688 |
| max_drawdown | 0.4472 |
| cagr | -0.1957 |
| net_avg_win | 71.8200 |
| net_avg_loss | -85.0983 |
| avg_hold_time_bars | 28.8586 |
| exposure | 0.6310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
