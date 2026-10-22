# EMA Hourly Continuation — MAGIC/USDT P34_100

**Symbol:** MAGIC/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.7127 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.9240 |
| gross_win_rate | 0.4750 |
| sharpe_ratio | -2.4107 |
| sortino_ratio | -0.7208 |
| max_drawdown | 0.5704 |
| cagr | -0.2825 |
| net_avg_win | 67.1305 |
| net_avg_loss | -85.2193 |
| avg_hold_time_bars | 15.3614 |
| exposure | 0.3072 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
