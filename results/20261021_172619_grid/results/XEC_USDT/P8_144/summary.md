# EMA Hourly Continuation — XEC/USDT P8_144

**Symbol:** XEC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.7715 |
| net_win_rate | 0.4968 |
| gross_profit_factor | 0.9806 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -1.7844 |
| sortino_ratio | -0.5503 |
| max_drawdown | 0.5346 |
| cagr | -0.2254 |
| net_avg_win | 68.8434 |
| net_avg_loss | -88.0937 |
| avg_hold_time_bars | 33.4776 |
| exposure | 0.7105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
