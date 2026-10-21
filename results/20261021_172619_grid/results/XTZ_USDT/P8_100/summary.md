# EMA Hourly Continuation — XTZ/USDT P8_100

**Symbol:** XTZ/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.7741 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 0.9940 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -1.6250 |
| sortino_ratio | -0.4967 |
| max_drawdown | 0.4615 |
| cagr | -0.2051 |
| net_avg_win | 65.8725 |
| net_avg_loss | -85.4664 |
| avg_hold_time_bars | 33.4703 |
| exposure | 0.6922 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
