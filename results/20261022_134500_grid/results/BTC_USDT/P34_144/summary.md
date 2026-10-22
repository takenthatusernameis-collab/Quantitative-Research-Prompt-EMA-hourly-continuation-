# EMA Hourly Continuation — BTC/USDT P34_144

**Symbol:** BTC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.4900 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 1.0733 |
| gross_win_rate | 0.5099 |
| sharpe_ratio | -4.8779 |
| sortino_ratio | -1.4320 |
| max_drawdown | 0.8758 |
| cagr | -0.5171 |
| net_avg_win | 35.7660 |
| net_avg_loss | -63.7634 |
| avg_hold_time_bars | 19.0694 |
| exposure | 0.3844 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
