# EMA Hourly Continuation — TRAC/USDT P89_200

**Symbol:** TRAC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.6683 |
| net_win_rate | 0.4976 |
| gross_profit_factor | 1.0064 |
| gross_win_rate | 0.5024 |
| sharpe_ratio | -2.5873 |
| sortino_ratio | -0.7514 |
| max_drawdown | 0.6007 |
| cagr | -0.2998 |
| net_avg_win | 56.4693 |
| net_avg_loss | -83.7023 |
| avg_hold_time_bars | 10.5613 |
| exposure | 0.2035 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
