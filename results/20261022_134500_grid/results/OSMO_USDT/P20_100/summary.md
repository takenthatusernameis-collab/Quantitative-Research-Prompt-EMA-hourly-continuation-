# EMA Hourly Continuation — OSMO/USDT P20_100

**Symbol:** OSMO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.6851 |
| net_win_rate | 0.4913 |
| gross_profit_factor | 1.0428 |
| gross_win_rate | 0.4976 |
| sharpe_ratio | -3.3976 |
| sortino_ratio | -1.2009 |
| max_drawdown | 0.7702 |
| cagr | -0.4387 |
| net_avg_win | 53.5520 |
| net_avg_loss | -75.4959 |
| avg_hold_time_bars | 15.7409 |
| exposure | 0.4529 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
