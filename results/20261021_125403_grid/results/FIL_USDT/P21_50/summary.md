# EMA Hourly Continuation — FIL/USDT P21_50

**Symbol:** FIL/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.7165 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9687 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -2.2120 |
| sortino_ratio | -0.6702 |
| max_drawdown | 0.5499 |
| cagr | -0.2641 |
| net_avg_win | 61.7001 |
| net_avg_loss | -83.4577 |
| avg_hold_time_bars | 6.9217 |
| exposure | 0.1406 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
