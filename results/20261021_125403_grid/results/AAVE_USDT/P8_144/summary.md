# EMA Hourly Continuation — AAVE/USDT P8_144

**Symbol:** AAVE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.9158 |
| net_win_rate | 0.5215 |
| gross_profit_factor | 1.0750 |
| gross_win_rate | 0.5215 |
| sharpe_ratio | -0.4452 |
| sortino_ratio | -0.1155 |
| max_drawdown | 0.2509 |
| cagr | -0.0555 |
| net_avg_win | 85.4640 |
| net_avg_loss | -101.7009 |
| avg_hold_time_bars | 50.8067 |
| exposure | 0.7529 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
