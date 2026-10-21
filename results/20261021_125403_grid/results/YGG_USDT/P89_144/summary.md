# EMA Hourly Continuation — YGG/USDT P89_144

**Symbol:** YGG/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.7990 |
| net_win_rate | 0.5204 |
| gross_profit_factor | 1.0652 |
| gross_win_rate | 0.5204 |
| sharpe_ratio | -1.1335 |
| sortino_ratio | -0.2791 |
| max_drawdown | 0.2906 |
| cagr | -0.1213 |
| net_avg_win | 72.2951 |
| net_avg_loss | -98.1847 |
| avg_hold_time_bars | 7.7279 |
| exposure | 0.1028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
