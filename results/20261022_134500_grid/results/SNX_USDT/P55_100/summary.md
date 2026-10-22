# EMA Hourly Continuation — SNX/USDT P55_100

**Symbol:** SNX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.6413 |
| net_win_rate | 0.5071 |
| gross_profit_factor | 1.1472 |
| gross_win_rate | 0.5213 |
| sharpe_ratio | -4.0057 |
| sortino_ratio | -1.4069 |
| max_drawdown | 0.8299 |
| cagr | -0.5007 |
| net_avg_win | 46.0351 |
| net_avg_loss | -73.8555 |
| avg_hold_time_bars | 4.7773 |
| exposure | 0.1368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
