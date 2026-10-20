# EMA Hourly Continuation — MASK/USDT P20_21

**Symbol:** MASK/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1221 |
| net_profit_factor | 0.0746 |
| net_win_rate | 0.2957 |
| gross_profit_factor | 0.3941 |
| gross_win_rate | 0.4013 |
| sharpe_ratio | -18.0281 |
| sortino_ratio | -9.6458 |
| max_drawdown | 1.0000 |
| cagr | -0.9955 |
| net_avg_win | 2.2329 |
| net_avg_loss | -12.5652 |
| avg_hold_time_bars | 2.2523 |
| exposure | 0.1250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
