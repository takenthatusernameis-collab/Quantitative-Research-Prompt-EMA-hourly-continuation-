# EMA Hourly Continuation — NEAR/USDT P26_144

**Symbol:** NEAR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7750 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 0.9172 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -1.4809 |
| sortino_ratio | -0.3946 |
| max_drawdown | 0.4344 |
| cagr | -0.1674 |
| net_avg_win | 75.5885 |
| net_avg_loss | -90.0317 |
| avg_hold_time_bars | 28.5400 |
| exposure | 0.4540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
