# EMA Hourly Continuation — JUP/USDT P100_144

**Symbol:** JUP/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.4586 |
| net_win_rate | 0.4265 |
| gross_profit_factor | 0.7908 |
| gross_win_rate | 0.4286 |
| sharpe_ratio | -5.6339 |
| sortino_ratio | -1.7526 |
| max_drawdown | 0.8902 |
| cagr | -0.5818 |
| net_avg_win | 35.9928 |
| net_avg_loss | -58.3725 |
| avg_hold_time_bars | 3.8857 |
| exposure | 0.0865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
