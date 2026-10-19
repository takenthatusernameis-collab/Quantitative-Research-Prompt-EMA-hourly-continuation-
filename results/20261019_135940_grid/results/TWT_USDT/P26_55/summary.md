# EMA Hourly Continuation — TWT/USDT P26_55

**Symbol:** TWT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 958 |
| net_profit_factor | 0.3723 |
| net_win_rate | 0.4530 |
| gross_profit_factor | 0.8031 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -8.3090 |
| sortino_ratio | -3.6342 |
| max_drawdown | 0.9903 |
| cagr | -0.8386 |
| net_avg_win | 13.5265 |
| net_avg_loss | -30.0915 |
| avg_hold_time_bars | 4.3309 |
| exposure | 0.1886 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
