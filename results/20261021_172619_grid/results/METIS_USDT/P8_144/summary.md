# EMA Hourly Continuation — METIS/USDT P8_144

**Symbol:** METIS/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.7900 |
| net_win_rate | 0.4804 |
| gross_profit_factor | 0.9308 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -1.4935 |
| sortino_ratio | -0.4019 |
| max_drawdown | 0.4228 |
| cagr | -0.1701 |
| net_avg_win | 81.7516 |
| net_avg_loss | -95.6962 |
| avg_hold_time_bars | 45.5922 |
| exposure | 0.7419 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
