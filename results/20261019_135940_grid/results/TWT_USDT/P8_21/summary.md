# EMA Hourly Continuation — TWT/USDT P8_21

**Symbol:** TWT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1783 |
| net_profit_factor | 0.2983 |
| net_win_rate | 0.4004 |
| gross_profit_factor | 0.7779 |
| gross_win_rate | 0.4436 |
| sharpe_ratio | -14.6400 |
| sortino_ratio | -8.8078 |
| max_drawdown | 1.0000 |
| cagr | -0.9892 |
| net_avg_win | 5.9533 |
| net_avg_loss | -13.3307 |
| avg_hold_time_bars | 2.8732 |
| exposure | 0.2329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
