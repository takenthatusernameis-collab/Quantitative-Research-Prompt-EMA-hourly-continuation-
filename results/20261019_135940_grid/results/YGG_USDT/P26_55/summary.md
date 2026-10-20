# EMA Hourly Continuation — YGG/USDT P26_55

**Symbol:** YGG/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 953 |
| net_profit_factor | 0.5815 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 0.9770 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -5.8743 |
| sortino_ratio | -2.5578 |
| max_drawdown | 0.9580 |
| cagr | -0.7063 |
| net_avg_win | 29.3424 |
| net_avg_loss | -45.5252 |
| avg_hold_time_bars | 4.3305 |
| exposure | 0.1868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
