# EMA Hourly Continuation — ETC/USDT P26_55

**Symbol:** ETC/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.5913 |
| net_win_rate | 0.4753 |
| gross_profit_factor | 0.9155 |
| gross_win_rate | 0.4753 |
| sharpe_ratio | -3.5051 |
| sortino_ratio | -1.0617 |
| max_drawdown | 0.7036 |
| cagr | -0.3838 |
| net_avg_win | 48.0054 |
| net_avg_loss | -73.5595 |
| avg_hold_time_bars | 6.1659 |
| exposure | 0.1250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
