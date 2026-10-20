# EMA Hourly Continuation — MEW/USDT P100_200

**Symbol:** MEW/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.6088 |
| net_win_rate | 0.4575 |
| gross_profit_factor | 0.8965 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -3.5179 |
| sortino_ratio | -0.9853 |
| max_drawdown | 0.7192 |
| cagr | -0.3802 |
| net_avg_win | 59.4553 |
| net_avg_loss | -82.3626 |
| avg_hold_time_bars | 9.8125 |
| exposure | 0.1784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
