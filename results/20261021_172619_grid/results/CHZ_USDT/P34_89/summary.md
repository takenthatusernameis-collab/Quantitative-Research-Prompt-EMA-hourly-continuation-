# EMA Hourly Continuation — CHZ/USDT P34_89

**Symbol:** CHZ/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.7320 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9547 |
| gross_win_rate | 0.4882 |
| sharpe_ratio | -2.0010 |
| sortino_ratio | -0.5891 |
| max_drawdown | 0.5077 |
| cagr | -0.2372 |
| net_avg_win | 65.1028 |
| net_avg_loss | -84.8381 |
| avg_hold_time_bars | 12.0165 |
| exposure | 0.2316 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
