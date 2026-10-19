# EMA Hourly Continuation — POL/USDT P12_50

**Symbol:** POL/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1060 |
| net_profit_factor | 0.3819 |
| net_win_rate | 0.4255 |
| gross_profit_factor | 0.7460 |
| gross_win_rate | 0.4462 |
| sharpe_ratio | -8.5724 |
| sortino_ratio | -3.9145 |
| max_drawdown | 0.9928 |
| cagr | -0.8588 |
| net_avg_win | 13.6002 |
| net_avg_loss | -26.3717 |
| avg_hold_time_bars | 8.1821 |
| exposure | 0.3942 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
