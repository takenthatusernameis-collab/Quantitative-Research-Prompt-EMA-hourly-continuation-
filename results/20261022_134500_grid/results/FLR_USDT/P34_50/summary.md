# EMA Hourly Continuation — FLR/USDT P34_50

**Symbol:** FLR/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1067 |
| net_profit_factor | 0.2941 |
| net_win_rate | 0.3683 |
| gross_profit_factor | 0.7374 |
| gross_win_rate | 0.4021 |
| sharpe_ratio | -12.8570 |
| sortino_ratio | -6.0700 |
| max_drawdown | 0.9996 |
| cagr | -0.9576 |
| net_avg_win | 10.5954 |
| net_avg_loss | -21.0095 |
| avg_hold_time_bars | 2.5736 |
| exposure | 0.1248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
