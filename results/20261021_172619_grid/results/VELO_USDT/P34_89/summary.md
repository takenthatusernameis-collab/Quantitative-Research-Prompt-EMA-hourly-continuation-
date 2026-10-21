# EMA Hourly Continuation — VELO/USDT P34_89

**Symbol:** VELO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.8251 |
| net_win_rate | 0.5024 |
| gross_profit_factor | 0.9993 |
| gross_win_rate | 0.5024 |
| sharpe_ratio | -1.1987 |
| sortino_ratio | -0.3492 |
| max_drawdown | 0.3865 |
| cagr | -0.1501 |
| net_avg_win | 76.0060 |
| net_avg_loss | -93.0165 |
| avg_hold_time_bars | 11.5314 |
| exposure | 0.2170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
