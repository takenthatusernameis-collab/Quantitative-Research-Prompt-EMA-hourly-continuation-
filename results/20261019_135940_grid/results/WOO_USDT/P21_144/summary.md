# EMA Hourly Continuation — WOO/USDT P21_144

**Symbol:** WOO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.7531 |
| net_win_rate | 0.4912 |
| gross_profit_factor | 1.0095 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -2.1139 |
| sortino_ratio | -0.6362 |
| max_drawdown | 0.5523 |
| cagr | -0.2580 |
| net_avg_win | 72.4625 |
| net_avg_loss | -92.8707 |
| avg_hold_time_bars | 26.8827 |
| exposure | 0.5523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
