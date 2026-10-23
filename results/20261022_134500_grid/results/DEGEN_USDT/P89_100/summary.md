# EMA Hourly Continuation — DEGEN/USDT P89_100

**Symbol:** DEGEN/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 574 |
| net_profit_factor | 0.4064 |
| net_win_rate | 0.4094 |
| gross_profit_factor | 0.7802 |
| gross_win_rate | 0.4268 |
| sharpe_ratio | -7.4600 |
| sortino_ratio | -2.5508 |
| max_drawdown | 0.9601 |
| cagr | -0.7226 |
| net_avg_win | 27.9628 |
| net_avg_loss | -47.6977 |
| avg_hold_time_bars | 2.7491 |
| exposure | 0.0718 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
