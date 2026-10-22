# EMA Hourly Continuation — PYTH/USDT P55_100

**Symbol:** PYTH/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.4975 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.8264 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -4.9696 |
| sortino_ratio | -1.7710 |
| max_drawdown | 0.8861 |
| cagr | -0.5731 |
| net_avg_win | 29.7040 |
| net_avg_loss | -51.0276 |
| avg_hold_time_bars | 5.0909 |
| exposure | 0.1476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
