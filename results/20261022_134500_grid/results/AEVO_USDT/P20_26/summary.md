# EMA Hourly Continuation — AEVO/USDT P20_26

**Symbol:** AEVO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1217 |
| net_profit_factor | 0.3084 |
| net_win_rate | 0.3796 |
| gross_profit_factor | 0.7772 |
| gross_win_rate | 0.4224 |
| sharpe_ratio | -13.0088 |
| sortino_ratio | -6.4905 |
| max_drawdown | 0.9998 |
| cagr | -0.9666 |
| net_avg_win | 9.6507 |
| net_avg_loss | -19.1480 |
| avg_hold_time_bars | 2.2572 |
| exposure | 0.1243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
