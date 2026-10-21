# EMA Hourly Continuation — BSV/USDT P20_144

**Symbol:** BSV/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.6195 |
| net_win_rate | 0.4336 |
| gross_profit_factor | 0.7837 |
| gross_win_rate | 0.4336 |
| sharpe_ratio | -3.2580 |
| sortino_ratio | -0.9458 |
| max_drawdown | 0.6708 |
| cagr | -0.3530 |
| net_avg_win | 59.1501 |
| net_avg_loss | -73.1105 |
| avg_hold_time_bars | 27.5450 |
| exposure | 0.5284 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
