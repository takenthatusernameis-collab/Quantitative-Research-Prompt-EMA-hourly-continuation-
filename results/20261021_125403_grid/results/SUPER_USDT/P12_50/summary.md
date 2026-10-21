# EMA Hourly Continuation — SUPER/USDT P12_50

**Symbol:** SUPER/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.8051 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 1.0280 |
| gross_win_rate | 0.5066 |
| sharpe_ratio | -1.9032 |
| sortino_ratio | -0.7126 |
| max_drawdown | 0.5941 |
| cagr | -0.2809 |
| net_avg_win | 67.4362 |
| net_avg_loss | -85.4933 |
| avg_hold_time_bars | 10.1098 |
| exposure | 0.3139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
