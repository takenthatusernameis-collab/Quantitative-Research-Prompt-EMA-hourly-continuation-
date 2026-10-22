# EMA Hourly Continuation — API3/USDT P12_55

**Symbol:** API3/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.7412 |
| net_win_rate | 0.4855 |
| gross_profit_factor | 0.9398 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -2.5057 |
| sortino_ratio | -0.9171 |
| max_drawdown | 0.6771 |
| cagr | -0.3442 |
| net_avg_win | 58.6493 |
| net_avg_loss | -74.6840 |
| avg_hold_time_bars | 12.2679 |
| exposure | 0.3664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
