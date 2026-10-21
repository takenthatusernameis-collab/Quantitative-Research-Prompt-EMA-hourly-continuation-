# EMA Hourly Continuation — MINA/USDT P8_20

**Symbol:** MINA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.7475 |
| net_win_rate | 0.5227 |
| gross_profit_factor | 1.0744 |
| gross_win_rate | 0.5227 |
| sharpe_ratio | -2.3085 |
| sortino_ratio | -0.8544 |
| max_drawdown | 0.6877 |
| cagr | -0.3240 |
| net_avg_win | 53.7074 |
| net_avg_loss | -78.6949 |
| avg_hold_time_bars | 5.3091 |
| exposure | 0.1593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
