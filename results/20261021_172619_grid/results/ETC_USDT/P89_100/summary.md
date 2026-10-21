# EMA Hourly Continuation — ETC/USDT P89_100

**Symbol:** ETC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 90 |
| net_profit_factor | 0.5538 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.8979 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -1.6541 |
| sortino_ratio | -0.2260 |
| max_drawdown | 0.2281 |
| cagr | -0.0980 |
| net_avg_win | 65.8514 |
| net_avg_loss | -108.7878 |
| avg_hold_time_bars | 6.1000 |
| exposure | 0.0250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
