# EMA Hourly Continuation — PYTH/USDT P12_55

**Symbol:** PYTH/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.5984 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.9141 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -5.2334 |
| sortino_ratio | -2.3220 |
| max_drawdown | 0.9433 |
| cagr | -0.6768 |
| net_avg_win | 29.4036 |
| net_avg_loss | -44.3927 |
| avg_hold_time_bars | 7.9881 |
| exposure | 0.3649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
