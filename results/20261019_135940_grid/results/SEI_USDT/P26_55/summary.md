# EMA Hourly Continuation — SEI/USDT P26_55

**Symbol:** SEI/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 918 |
| net_profit_factor | 0.4988 |
| net_win_rate | 0.4662 |
| gross_profit_factor | 0.8667 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -6.6816 |
| sortino_ratio | -2.8406 |
| max_drawdown | 0.9726 |
| cagr | -0.7554 |
| net_avg_win | 22.5788 |
| net_avg_loss | -39.5359 |
| avg_hold_time_bars | 4.1394 |
| exposure | 0.1727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
