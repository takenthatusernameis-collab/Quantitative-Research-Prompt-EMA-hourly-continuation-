# EMA Hourly Continuation — LUNA/USDT P144_200

**Symbol:** LUNA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.4282 |
| net_win_rate | 0.4427 |
| gross_profit_factor | 0.8530 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -5.6250 |
| sortino_ratio | -1.6842 |
| max_drawdown | 0.8879 |
| cagr | -0.5758 |
| net_avg_win | 32.9339 |
| net_avg_loss | -61.1021 |
| avg_hold_time_bars | 4.9493 |
| exposure | 0.1021 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
