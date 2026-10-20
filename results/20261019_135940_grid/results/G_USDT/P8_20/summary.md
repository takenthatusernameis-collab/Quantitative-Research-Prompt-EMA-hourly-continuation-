# EMA Hourly Continuation — G/USDT P8_20

**Symbol:** G/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1224 |
| net_profit_factor | 0.4240 |
| net_win_rate | 0.4526 |
| gross_profit_factor | 0.9089 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -9.9181 |
| sortino_ratio | -5.2661 |
| max_drawdown | 0.9967 |
| cagr | -0.9280 |
| net_avg_win | 13.2435 |
| net_avg_loss | -25.8267 |
| avg_hold_time_bars | 4.0384 |
| exposure | 0.2599 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
