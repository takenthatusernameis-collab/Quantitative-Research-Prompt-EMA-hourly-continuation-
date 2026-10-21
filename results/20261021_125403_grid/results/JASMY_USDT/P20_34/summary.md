# EMA Hourly Continuation — JASMY/USDT P20_34

**Symbol:** JASMY/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.7290 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9638 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -1.5600 |
| sortino_ratio | -0.3535 |
| max_drawdown | 0.3379 |
| cagr | -0.1495 |
| net_avg_win | 73.0735 |
| net_avg_loss | -97.0750 |
| avg_hold_time_bars | 4.9880 |
| exposure | 0.0567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
