# EMA Hourly Continuation — INJ/USDT P50_100

**Symbol:** INJ/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.7986 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0076 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.3670 |
| sortino_ratio | -0.3624 |
| max_drawdown | 0.4067 |
| cagr | -0.1538 |
| net_avg_win | 79.4344 |
| net_avg_loss | -99.4713 |
| avg_hold_time_bars | 7.5673 |
| exposure | 0.1176 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
