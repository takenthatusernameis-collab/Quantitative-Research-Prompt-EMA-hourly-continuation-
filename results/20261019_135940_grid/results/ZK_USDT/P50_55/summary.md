# EMA Hourly Continuation — ZK/USDT P50_55

**Symbol:** ZK/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 793 |
| net_profit_factor | 0.3138 |
| net_win_rate | 0.3859 |
| gross_profit_factor | 0.8415 |
| gross_win_rate | 0.4338 |
| sharpe_ratio | -10.8994 |
| sortino_ratio | -4.5695 |
| max_drawdown | 0.9967 |
| cagr | -0.9116 |
| net_avg_win | 14.8918 |
| net_avg_loss | -29.8208 |
| avg_hold_time_bars | 2.3783 |
| exposure | 0.0920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
