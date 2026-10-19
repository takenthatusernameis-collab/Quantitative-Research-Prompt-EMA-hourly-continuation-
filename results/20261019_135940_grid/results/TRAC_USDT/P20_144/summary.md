# EMA Hourly Continuation — TRAC/USDT P20_144

**Symbol:** TRAC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.7075 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9885 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -2.7398 |
| sortino_ratio | -0.8876 |
| max_drawdown | 0.6641 |
| cagr | -0.3456 |
| net_avg_win | 60.9609 |
| net_avg_loss | -82.3613 |
| avg_hold_time_bars | 20.9361 |
| exposure | 0.5063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
