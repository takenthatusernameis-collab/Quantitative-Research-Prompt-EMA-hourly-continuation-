# EMA Hourly Continuation — POKT/USDT P34_89

**Symbol:** POKT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.6776 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.8805 |
| gross_win_rate | 0.4500 |
| sharpe_ratio | -3.0709 |
| sortino_ratio | -0.9314 |
| max_drawdown | 0.6760 |
| cagr | -0.3496 |
| net_avg_win | 67.2184 |
| net_avg_loss | -81.1695 |
| avg_hold_time_bars | 12.4391 |
| exposure | 0.2589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
