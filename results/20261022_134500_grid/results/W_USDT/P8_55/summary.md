# EMA Hourly Continuation — W/USDT P8_55

**Symbol:** W/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 977 |
| net_profit_factor | 0.6429 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.9338 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -4.4522 |
| sortino_ratio | -1.9509 |
| max_drawdown | 0.9097 |
| cagr | -0.6089 |
| net_avg_win | 35.0574 |
| net_avg_loss | -49.5215 |
| avg_hold_time_bars | 11.2252 |
| exposure | 0.4985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
