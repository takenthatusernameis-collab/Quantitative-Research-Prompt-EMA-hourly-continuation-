# EMA Hourly Continuation — RPL/USDT P50_200

**Symbol:** RPL/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.8275 |
| net_win_rate | 0.4967 |
| gross_profit_factor | 0.9984 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -1.0800 |
| sortino_ratio | -0.2686 |
| max_drawdown | 0.3434 |
| cagr | -0.1177 |
| net_avg_win | 86.0265 |
| net_avg_loss | -102.5988 |
| avg_hold_time_bars | 30.9704 |
| exposure | 0.4261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
