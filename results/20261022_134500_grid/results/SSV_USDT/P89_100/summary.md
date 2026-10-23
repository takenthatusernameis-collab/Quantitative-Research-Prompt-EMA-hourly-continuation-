# EMA Hourly Continuation — SSV/USDT P89_100

**Symbol:** SSV/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.2878 |
| net_win_rate | 0.4038 |
| gross_profit_factor | 0.7858 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -9.1116 |
| sortino_ratio | -3.3925 |
| max_drawdown | 0.9890 |
| cagr | -0.8321 |
| net_avg_win | 14.5285 |
| net_avg_loss | -34.1978 |
| avg_hold_time_bars | 2.1821 |
| exposure | 0.0672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
