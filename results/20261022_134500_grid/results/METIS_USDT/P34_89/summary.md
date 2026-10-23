# EMA Hourly Continuation — METIS/USDT P34_89

**Symbol:** METIS/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.5252 |
| net_win_rate | 0.4378 |
| gross_profit_factor | 0.8727 |
| gross_win_rate | 0.4476 |
| sharpe_ratio | -5.9039 |
| sortino_ratio | -2.2255 |
| max_drawdown | 0.9352 |
| cagr | -0.6587 |
| net_avg_win | 32.9650 |
| net_avg_loss | -48.8699 |
| avg_hold_time_bars | 7.4252 |
| exposure | 0.2413 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
