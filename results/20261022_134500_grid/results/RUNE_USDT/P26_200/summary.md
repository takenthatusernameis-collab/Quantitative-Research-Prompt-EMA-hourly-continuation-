# EMA Hourly Continuation — RUNE/USDT P26_200

**Symbol:** RUNE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.7097 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9762 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.7084 |
| sortino_ratio | -0.4174 |
| max_drawdown | 0.4133 |
| cagr | -0.1800 |
| net_avg_win | 65.2745 |
| net_avg_loss | -88.3705 |
| avg_hold_time_bars | 47.8900 |
| exposure | 0.6530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
