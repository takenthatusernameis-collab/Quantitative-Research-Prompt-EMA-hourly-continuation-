# EMA Hourly Continuation — KMNO/USDT P34_55

**Symbol:** KMNO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.7027 |
| net_win_rate | 0.4985 |
| gross_profit_factor | 1.0010 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -2.0912 |
| sortino_ratio | -0.5505 |
| max_drawdown | 0.4899 |
| cagr | -0.2246 |
| net_avg_win | 66.4791 |
| net_avg_loss | -94.0347 |
| avg_hold_time_bars | 5.6907 |
| exposure | 0.0875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
