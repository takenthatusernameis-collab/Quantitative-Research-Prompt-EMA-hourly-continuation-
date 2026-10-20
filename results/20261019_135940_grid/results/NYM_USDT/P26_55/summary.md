# EMA Hourly Continuation — NYM/USDT P26_55

**Symbol:** NYM/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 785 |
| net_profit_factor | 0.2296 |
| net_win_rate | 0.2981 |
| gross_profit_factor | 0.6392 |
| gross_win_rate | 0.3643 |
| sharpe_ratio | -12.6210 |
| sortino_ratio | -5.1620 |
| max_drawdown | 0.9990 |
| cagr | -0.9366 |
| net_avg_win | 12.7244 |
| net_avg_loss | -23.5349 |
| avg_hold_time_bars | 6.3924 |
| exposure | 0.2281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
