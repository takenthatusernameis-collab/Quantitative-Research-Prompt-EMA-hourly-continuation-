# EMA Hourly Continuation — LQTY/USDT P55_89

**Symbol:** LQTY/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.4249 |
| net_win_rate | 0.4173 |
| gross_profit_factor | 0.7294 |
| gross_win_rate | 0.4317 |
| sharpe_ratio | -6.9641 |
| sortino_ratio | -2.6031 |
| max_drawdown | 0.9575 |
| cagr | -0.7125 |
| net_avg_win | 24.3835 |
| net_avg_loss | -41.0874 |
| avg_hold_time_bars | 4.4662 |
| exposure | 0.1405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
