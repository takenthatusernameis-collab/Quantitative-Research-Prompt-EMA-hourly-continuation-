# EMA Hourly Continuation — KAVA/USDT P26_34

**Symbol:** KAVA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.4687 |
| net_win_rate | 0.4247 |
| gross_profit_factor | 0.8400 |
| gross_win_rate | 0.4363 |
| sharpe_ratio | -4.2771 |
| sortino_ratio | -0.9907 |
| max_drawdown | 0.7014 |
| cagr | -0.3745 |
| net_avg_win | 55.5076 |
| net_avg_loss | -87.4362 |
| avg_hold_time_bars | 6.5521 |
| exposure | 0.0771 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
