# EMA Hourly Continuation — TWT/USDT P8_34

**Symbol:** TWT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1492 |
| net_profit_factor | 0.3615 |
| net_win_rate | 0.4424 |
| gross_profit_factor | 0.7942 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -10.4272 |
| sortino_ratio | -5.6569 |
| max_drawdown | 0.9992 |
| cagr | -0.9420 |
| net_avg_win | 8.5714 |
| net_avg_loss | -18.8092 |
| avg_hold_time_bars | 5.2011 |
| exposure | 0.3527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
