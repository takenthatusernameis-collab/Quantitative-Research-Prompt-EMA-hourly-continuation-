# EMA Hourly Continuation — DOT/USDT P26_144

**Symbol:** DOT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.6153 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.9307 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -3.4037 |
| sortino_ratio | -1.0270 |
| max_drawdown | 0.7250 |
| cagr | -0.3924 |
| net_avg_win | 52.6231 |
| net_avg_loss | -75.4371 |
| avg_hold_time_bars | 23.2851 |
| exposure | 0.4900 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
