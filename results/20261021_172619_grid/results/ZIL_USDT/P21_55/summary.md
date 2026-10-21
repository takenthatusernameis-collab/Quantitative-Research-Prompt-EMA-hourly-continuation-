# EMA Hourly Continuation — ZIL/USDT P21_55

**Symbol:** ZIL/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.7114 |
| net_win_rate | 0.4933 |
| gross_profit_factor | 0.9828 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -2.5426 |
| sortino_ratio | -0.8339 |
| max_drawdown | 0.6583 |
| cagr | -0.3176 |
| net_avg_win | 58.9447 |
| net_avg_loss | -80.6719 |
| avg_hold_time_bars | 8.4608 |
| exposure | 0.2011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
