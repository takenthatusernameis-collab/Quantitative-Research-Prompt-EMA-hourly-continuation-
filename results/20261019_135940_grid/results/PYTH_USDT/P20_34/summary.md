# EMA Hourly Continuation — PYTH/USDT P20_34

**Symbol:** PYTH/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1128 |
| net_profit_factor | 0.4411 |
| net_win_rate | 0.4477 |
| gross_profit_factor | 0.8825 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -8.7462 |
| sortino_ratio | -4.1304 |
| max_drawdown | 0.9946 |
| cagr | -0.8744 |
| net_avg_win | 15.5406 |
| net_avg_loss | -28.5609 |
| avg_hold_time_bars | 2.4973 |
| exposure | 0.1280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
