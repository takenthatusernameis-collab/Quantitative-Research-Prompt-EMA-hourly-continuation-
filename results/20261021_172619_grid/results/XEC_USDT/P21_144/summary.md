# EMA Hourly Continuation — XEC/USDT P21_144

**Symbol:** XEC/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.7978 |
| net_win_rate | 0.5045 |
| gross_profit_factor | 1.0230 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -1.5492 |
| sortino_ratio | -0.4657 |
| max_drawdown | 0.5107 |
| cagr | -0.1938 |
| net_avg_win | 74.1636 |
| net_avg_loss | -94.6581 |
| avg_hold_time_bars | 26.5407 |
| exposure | 0.5308 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
