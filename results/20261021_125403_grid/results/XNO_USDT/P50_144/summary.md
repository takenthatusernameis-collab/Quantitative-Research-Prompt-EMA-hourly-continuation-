# EMA Hourly Continuation — XNO/USDT P50_144

**Symbol:** XNO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.6523 |
| net_win_rate | 0.4424 |
| gross_profit_factor | 0.8280 |
| gross_win_rate | 0.4424 |
| sharpe_ratio | -2.8776 |
| sortino_ratio | -0.7976 |
| max_drawdown | 0.6061 |
| cagr | -0.3075 |
| net_avg_win | 66.9112 |
| net_avg_loss | -81.3817 |
| avg_hold_time_bars | 14.7330 |
| exposure | 0.2558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
