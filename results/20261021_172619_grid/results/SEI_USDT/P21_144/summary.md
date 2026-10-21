# EMA Hourly Continuation — SEI/USDT P21_144

**Symbol:** SEI/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.9710 |
| net_win_rate | 0.5371 |
| gross_profit_factor | 1.1458 |
| gross_win_rate | 0.5371 |
| sharpe_ratio | -0.1296 |
| sortino_ratio | -0.0343 |
| max_drawdown | 0.2617 |
| cagr | -0.0215 |
| net_avg_win | 98.2413 |
| net_avg_loss | -117.3885 |
| avg_hold_time_bars | 36.9228 |
| exposure | 0.5656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
