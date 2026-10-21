# EMA Hourly Continuation — CELO/USDT P21_26

**Symbol:** CELO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.5487 |
| net_win_rate | 0.4528 |
| gross_profit_factor | 0.8278 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -2.9764 |
| sortino_ratio | -0.6779 |
| max_drawdown | 0.5551 |
| cagr | -0.2683 |
| net_avg_win | 57.6509 |
| net_avg_loss | -86.9295 |
| avg_hold_time_bars | 4.0433 |
| exposure | 0.0465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
