# EMA Hourly Continuation — ARB/USDT P26_89

**Symbol:** ARB/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.6126 |
| net_win_rate | 0.4919 |
| gross_profit_factor | 0.9898 |
| gross_win_rate | 0.4993 |
| sharpe_ratio | -3.7679 |
| sortino_ratio | -1.3889 |
| max_drawdown | 0.8116 |
| cagr | -0.4836 |
| net_avg_win | 38.3353 |
| net_avg_loss | -60.5850 |
| avg_hold_time_bars | 10.3888 |
| exposure | 0.3206 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
