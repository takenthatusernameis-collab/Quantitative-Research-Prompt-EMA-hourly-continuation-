# EMA Hourly Continuation — FLUX/USDT P20_144

**Symbol:** FLUX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.8114 |
| net_win_rate | 0.4962 |
| gross_profit_factor | 0.9878 |
| gross_win_rate | 0.4962 |
| sharpe_ratio | -1.3151 |
| sortino_ratio | -0.3758 |
| max_drawdown | 0.3974 |
| cagr | -0.1598 |
| net_avg_win | 76.9556 |
| net_avg_loss | -93.4279 |
| avg_hold_time_bars | 30.3283 |
| exposure | 0.5500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
