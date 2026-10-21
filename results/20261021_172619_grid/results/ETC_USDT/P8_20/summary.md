# EMA Hourly Continuation — ETC/USDT P8_20

**Symbol:** ETC/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.6474 |
| net_win_rate | 0.5114 |
| gross_profit_factor | 1.0309 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -2.9997 |
| sortino_ratio | -0.9955 |
| max_drawdown | 0.6824 |
| cagr | -0.3629 |
| net_avg_win | 46.0860 |
| net_avg_loss | -74.4948 |
| avg_hold_time_bars | 5.5909 |
| exposure | 0.1342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
