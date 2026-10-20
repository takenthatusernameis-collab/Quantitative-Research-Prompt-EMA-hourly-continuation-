# EMA Hourly Continuation — AURORA/USDT P34_55

**Symbol:** AURORA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 732 |
| net_profit_factor | 0.3603 |
| net_win_rate | 0.3852 |
| gross_profit_factor | 0.7761 |
| gross_win_rate | 0.4112 |
| sharpe_ratio | -9.3597 |
| sortino_ratio | -3.6323 |
| max_drawdown | 0.9907 |
| cagr | -0.8420 |
| net_avg_win | 19.7751 |
| net_avg_loss | -34.3985 |
| avg_hold_time_bars | 4.6298 |
| exposure | 0.1540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
