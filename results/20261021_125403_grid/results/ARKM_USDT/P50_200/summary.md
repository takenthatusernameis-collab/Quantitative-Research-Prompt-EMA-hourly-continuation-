# EMA Hourly Continuation — ARKM/USDT P50_200

**Symbol:** ARKM/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.8247 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9704 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.9302 |
| sortino_ratio | -0.2296 |
| max_drawdown | 0.2788 |
| cagr | -0.1017 |
| net_avg_win | 75.0609 |
| net_avg_loss | -89.8072 |
| avg_hold_time_bars | 28.1678 |
| exposure | 0.3815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
