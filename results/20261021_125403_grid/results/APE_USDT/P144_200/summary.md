# EMA Hourly Continuation — APE/USDT P144_200

**Symbol:** APE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 201 |
| net_profit_factor | 0.7347 |
| net_win_rate | 0.5025 |
| gross_profit_factor | 0.9835 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -1.2450 |
| sortino_ratio | -0.2535 |
| max_drawdown | 0.2806 |
| cagr | -0.1097 |
| net_avg_win | 69.3958 |
| net_avg_loss | -95.4028 |
| avg_hold_time_bars | 6.6368 |
| exposure | 0.0606 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
