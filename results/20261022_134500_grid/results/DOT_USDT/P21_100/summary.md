# EMA Hourly Continuation — DOT/USDT P21_100

**Symbol:** DOT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.6798 |
| net_win_rate | 0.5049 |
| gross_profit_factor | 1.0716 |
| gross_win_rate | 0.5098 |
| sharpe_ratio | -3.2138 |
| sortino_ratio | -1.1173 |
| max_drawdown | 0.7611 |
| cagr | -0.4152 |
| net_avg_win | 51.0173 |
| net_avg_loss | -76.5369 |
| avg_hold_time_bars | 15.5967 |
| exposure | 0.4325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
