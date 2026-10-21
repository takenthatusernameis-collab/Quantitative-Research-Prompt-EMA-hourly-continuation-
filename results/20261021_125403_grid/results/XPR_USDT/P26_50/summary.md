# EMA Hourly Continuation — XPR/USDT P26_50

**Symbol:** XPR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 246 |
| net_profit_factor | 0.7717 |
| net_win_rate | 0.5163 |
| gross_profit_factor | 1.0655 |
| gross_win_rate | 0.5163 |
| sharpe_ratio | -1.2859 |
| sortino_ratio | -0.2904 |
| max_drawdown | 0.3177 |
| cagr | -0.1249 |
| net_avg_win | 75.7729 |
| net_avg_loss | -104.7931 |
| avg_hold_time_bars | 11.0203 |
| exposure | 0.1232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
