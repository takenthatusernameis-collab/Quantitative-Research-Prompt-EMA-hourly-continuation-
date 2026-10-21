# EMA Hourly Continuation — ADA/USDT P26_55

**Symbol:** ADA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.7130 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 0.9896 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -2.0087 |
| sortino_ratio | -0.5702 |
| max_drawdown | 0.4887 |
| cagr | -0.2288 |
| net_avg_win | 60.7534 |
| net_avg_loss | -85.6435 |
| avg_hold_time_bars | 7.6982 |
| exposure | 0.1368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
