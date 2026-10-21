# EMA Hourly Continuation — LISTA/USDT P55_200

**Symbol:** LISTA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.8039 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 0.9767 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -1.1655 |
| sortino_ratio | -0.3048 |
| max_drawdown | 0.2815 |
| cagr | -0.1320 |
| net_avg_win | 74.9354 |
| net_avg_loss | -91.4313 |
| avg_hold_time_bars | 23.7621 |
| exposure | 0.3614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
