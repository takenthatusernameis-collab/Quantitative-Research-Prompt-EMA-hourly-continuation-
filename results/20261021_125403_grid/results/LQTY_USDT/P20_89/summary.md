# EMA Hourly Continuation — LQTY/USDT P20_89

**Symbol:** LQTY/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.7084 |
| net_win_rate | 0.4692 |
| gross_profit_factor | 0.8849 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -2.5067 |
| sortino_ratio | -0.7979 |
| max_drawdown | 0.6180 |
| cagr | -0.3078 |
| net_avg_win | 62.2620 |
| net_avg_loss | -77.6814 |
| avg_hold_time_bars | 18.1074 |
| exposure | 0.4121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
