# EMA Hourly Continuation — CFX/USDT P12_144

**Symbol:** CFX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.6460 |
| net_win_rate | 0.4789 |
| gross_profit_factor | 0.9155 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -2.8756 |
| sortino_ratio | -0.8562 |
| max_drawdown | 0.6554 |
| cagr | -0.3356 |
| net_avg_win | 54.2230 |
| net_avg_loss | -77.1510 |
| avg_hold_time_bars | 33.0532 |
| exposure | 0.6776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
