# EMA Hourly Continuation — HNT/USDT P8_26

**Symbol:** HNT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 603 |
| net_profit_factor | 0.7038 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.9144 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -2.9153 |
| sortino_ratio | -1.0211 |
| max_drawdown | 0.6909 |
| cagr | -0.3733 |
| net_avg_win | 57.5750 |
| net_avg_loss | -73.3196 |
| avg_hold_time_bars | 8.2869 |
| exposure | 0.2271 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
