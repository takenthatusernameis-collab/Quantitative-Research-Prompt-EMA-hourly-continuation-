# EMA Hourly Continuation — POPCAT/USDT P89_100

**Symbol:** POPCAT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 576 |
| net_profit_factor | 0.4088 |
| net_win_rate | 0.4097 |
| gross_profit_factor | 0.7190 |
| gross_win_rate | 0.4392 |
| sharpe_ratio | -7.5024 |
| sortino_ratio | -2.7515 |
| max_drawdown | 0.9486 |
| cagr | -0.7460 |
| net_avg_win | 27.7884 |
| net_avg_loss | -47.1778 |
| avg_hold_time_bars | 2.1181 |
| exposure | 0.0644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
