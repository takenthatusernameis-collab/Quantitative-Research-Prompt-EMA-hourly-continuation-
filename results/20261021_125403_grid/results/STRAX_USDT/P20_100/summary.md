# EMA Hourly Continuation — STRAX/USDT P20_100

**Symbol:** STRAX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.6543 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.8585 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -3.5250 |
| sortino_ratio | -1.1704 |
| max_drawdown | 0.7562 |
| cagr | -0.4166 |
| net_avg_win | 57.1413 |
| net_avg_loss | -71.5575 |
| avg_hold_time_bars | 15.5129 |
| exposure | 0.3858 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
