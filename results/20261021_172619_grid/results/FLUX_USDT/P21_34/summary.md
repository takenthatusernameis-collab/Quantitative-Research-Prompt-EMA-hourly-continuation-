# EMA Hourly Continuation — FLUX/USDT P21_34

**Symbol:** FLUX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.6792 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 0.9348 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -2.0659 |
| sortino_ratio | -0.5067 |
| max_drawdown | 0.4863 |
| cagr | -0.2068 |
| net_avg_win | 65.7864 |
| net_avg_loss | -91.0828 |
| avg_hold_time_bars | 4.4573 |
| exposure | 0.0594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
