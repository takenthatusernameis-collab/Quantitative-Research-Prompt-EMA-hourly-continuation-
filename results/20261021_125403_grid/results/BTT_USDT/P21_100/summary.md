# EMA Hourly Continuation — BTT/USDT P21_100

**Symbol:** BTT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.5274 |
| net_win_rate | 0.4336 |
| gross_profit_factor | 0.8309 |
| gross_win_rate | 0.4360 |
| sharpe_ratio | -4.8875 |
| sortino_ratio | -1.4359 |
| max_drawdown | 0.8215 |
| cagr | -0.4930 |
| net_avg_win | 49.8950 |
| net_avg_loss | -72.4444 |
| avg_hold_time_bars | 23.5758 |
| exposure | 0.4522 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
