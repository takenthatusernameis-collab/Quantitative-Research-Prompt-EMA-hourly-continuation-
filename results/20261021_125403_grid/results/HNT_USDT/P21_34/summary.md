# EMA Hourly Continuation — HNT/USDT P21_34

**Symbol:** HNT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.5249 |
| net_win_rate | 0.4241 |
| gross_profit_factor | 0.7087 |
| gross_win_rate | 0.4241 |
| sharpe_ratio | -3.1830 |
| sortino_ratio | -0.7693 |
| max_drawdown | 0.5868 |
| cagr | -0.2967 |
| net_avg_win | 52.7036 |
| net_avg_loss | -73.9562 |
| avg_hold_time_bars | 5.2379 |
| exposure | 0.0690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
