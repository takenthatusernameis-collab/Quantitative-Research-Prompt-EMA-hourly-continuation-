# EMA Hourly Continuation — HNT/USDT P34_200

**Symbol:** HNT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.5728 |
| net_win_rate | 0.4386 |
| gross_profit_factor | 0.7512 |
| gross_win_rate | 0.4413 |
| sharpe_ratio | -3.1640 |
| sortino_ratio | -0.8672 |
| max_drawdown | 0.6966 |
| cagr | -0.3401 |
| net_avg_win | 51.6961 |
| net_avg_loss | -70.5274 |
| avg_hold_time_bars | 30.1044 |
| exposure | 0.5241 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
