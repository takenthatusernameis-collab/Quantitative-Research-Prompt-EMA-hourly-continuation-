# EMA Hourly Continuation — RAY/USDT P100_200

**Symbol:** RAY/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 0.7897 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9904 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.1195 |
| sortino_ratio | -0.2562 |
| max_drawdown | 0.3208 |
| cagr | -0.1122 |
| net_avg_win | 75.7848 |
| net_avg_loss | -95.9617 |
| avg_hold_time_bars | 12.0469 |
| exposure | 0.1402 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
