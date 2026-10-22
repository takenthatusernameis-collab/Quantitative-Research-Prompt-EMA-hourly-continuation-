# EMA Hourly Continuation — IOTA/USDT P34_144

**Symbol:** IOTA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.6142 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.9058 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -3.4746 |
| sortino_ratio | -1.0812 |
| max_drawdown | 0.7420 |
| cagr | -0.4014 |
| net_avg_win | 51.0275 |
| net_avg_loss | -72.4952 |
| avg_hold_time_bars | 17.8330 |
| exposure | 0.3931 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
