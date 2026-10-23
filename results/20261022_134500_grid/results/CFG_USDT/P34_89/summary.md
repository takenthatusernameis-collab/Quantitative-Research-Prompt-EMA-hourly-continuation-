# EMA Hourly Continuation — CFG/USDT P34_89

**Symbol:** CFG/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 751 |
| net_profit_factor | 0.5942 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.9102 |
| gross_win_rate | 0.4700 |
| sharpe_ratio | -4.5896 |
| sortino_ratio | -1.7658 |
| max_drawdown | 0.8925 |
| cagr | -0.5722 |
| net_avg_win | 36.9776 |
| net_avg_loss | -54.0286 |
| avg_hold_time_bars | 6.6924 |
| exposure | 0.2285 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
