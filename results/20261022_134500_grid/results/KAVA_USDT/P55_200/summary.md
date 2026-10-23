# EMA Hourly Continuation — KAVA/USDT P55_200

**Symbol:** KAVA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.5390 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.9137 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -4.2923 |
| sortino_ratio | -1.2107 |
| max_drawdown | 0.7803 |
| cagr | -0.4483 |
| net_avg_win | 49.8232 |
| net_avg_loss | -75.7765 |
| avg_hold_time_bars | 21.9901 |
| exposure | 0.4038 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
