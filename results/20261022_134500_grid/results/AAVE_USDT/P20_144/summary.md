# EMA Hourly Continuation — AAVE/USDT P20_144

**Symbol:** AAVE/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.6530 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 0.9491 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -2.9770 |
| sortino_ratio | -0.9487 |
| max_drawdown | 0.7104 |
| cagr | -0.3688 |
| net_avg_win | 50.7605 |
| net_avg_loss | -74.7869 |
| avg_hold_time_bars | 21.6390 |
| exposure | 0.5095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
