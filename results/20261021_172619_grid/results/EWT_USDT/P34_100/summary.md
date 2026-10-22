# EMA Hourly Continuation — EWT/USDT P34_100

**Symbol:** EWT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.7372 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 0.9221 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -1.8556 |
| sortino_ratio | -0.5201 |
| max_drawdown | 0.4794 |
| cagr | -0.2134 |
| net_avg_win | 68.2898 |
| net_avg_loss | -86.1455 |
| avg_hold_time_bars | 11.4482 |
| exposure | 0.2009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
