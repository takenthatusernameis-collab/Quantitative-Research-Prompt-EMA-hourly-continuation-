# EMA Hourly Continuation — DOT/USDT P20_26

**Symbol:** DOT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1180 |
| net_profit_factor | 0.1763 |
| net_win_rate | 0.3686 |
| gross_profit_factor | 0.7275 |
| gross_win_rate | 0.4178 |
| sharpe_ratio | -14.6840 |
| sortino_ratio | -7.3800 |
| max_drawdown | 1.0000 |
| cagr | -0.9818 |
| net_avg_win | 4.9207 |
| net_avg_loss | -16.2954 |
| avg_hold_time_bars | 1.8729 |
| exposure | 0.1005 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
