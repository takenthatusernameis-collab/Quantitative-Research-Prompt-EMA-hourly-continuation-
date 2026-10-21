# EMA Hourly Continuation — ELON/USDT P34_100

**Symbol:** ELON/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.7158 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 0.9297 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -1.9796 |
| sortino_ratio | -0.5606 |
| max_drawdown | 0.5040 |
| cagr | -0.2261 |
| net_avg_win | 62.6001 |
| net_avg_loss | -83.1040 |
| avg_hold_time_bars | 11.8393 |
| exposure | 0.2110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
