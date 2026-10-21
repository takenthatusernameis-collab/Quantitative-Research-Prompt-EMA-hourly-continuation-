# EMA Hourly Continuation — DEXE/USDT P50_55

**Symbol:** DEXE/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 137 |
| net_profit_factor | 0.6196 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.8933 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -1.6933 |
| sortino_ratio | -0.2826 |
| max_drawdown | 0.2945 |
| cagr | -0.1233 |
| net_avg_win | 70.5338 |
| net_avg_loss | -102.7733 |
| avg_hold_time_bars | 18.0949 |
| exposure | 0.1127 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
