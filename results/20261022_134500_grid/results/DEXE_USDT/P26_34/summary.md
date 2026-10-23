# EMA Hourly Continuation — DEXE/USDT P26_34

**Symbol:** DEXE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1116 |
| net_profit_factor | 0.1744 |
| net_win_rate | 0.3477 |
| gross_profit_factor | 0.4767 |
| gross_win_rate | 0.3835 |
| sharpe_ratio | -14.0299 |
| sortino_ratio | -6.8167 |
| max_drawdown | 0.9999 |
| cagr | -0.9732 |
| net_avg_win | 5.4439 |
| net_avg_loss | -16.6362 |
| avg_hold_time_bars | 3.9875 |
| exposure | 0.2023 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
