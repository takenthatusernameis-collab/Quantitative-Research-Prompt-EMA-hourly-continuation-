# EMA Hourly Continuation — ARB/USDT P26_50

**Symbol:** ARB/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.8267 |
| net_win_rate | 0.5309 |
| gross_profit_factor | 1.1121 |
| gross_win_rate | 0.5309 |
| sharpe_ratio | -1.0164 |
| sortino_ratio | -0.2771 |
| max_drawdown | 0.3251 |
| cagr | -0.1207 |
| net_avg_win | 69.6882 |
| net_avg_loss | -95.3984 |
| avg_hold_time_bars | 6.9579 |
| exposure | 0.1126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
