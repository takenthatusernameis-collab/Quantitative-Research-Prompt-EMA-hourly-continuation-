# EMA Hourly Continuation — VELO/USDT P26_34

**Symbol:** VELO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1101 |
| net_profit_factor | 0.3590 |
| net_win_rate | 0.3824 |
| gross_profit_factor | 0.6728 |
| gross_win_rate | 0.4033 |
| sharpe_ratio | -11.6389 |
| sortino_ratio | -5.5301 |
| max_drawdown | 0.9991 |
| cagr | -0.9394 |
| net_avg_win | 13.2893 |
| net_avg_loss | -22.9206 |
| avg_hold_time_bars | 2.1362 |
| exposure | 0.1069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
