# EMA Hourly Continuation — SNX/USDT P26_89

**Symbol:** SNX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 731 |
| net_profit_factor | 0.6755 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 1.0630 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -4.0579 |
| sortino_ratio | -1.5269 |
| max_drawdown | 0.8532 |
| cagr | -0.5272 |
| net_avg_win | 49.3552 |
| net_avg_loss | -70.1284 |
| avg_hold_time_bars | 8.9029 |
| exposure | 0.2945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
