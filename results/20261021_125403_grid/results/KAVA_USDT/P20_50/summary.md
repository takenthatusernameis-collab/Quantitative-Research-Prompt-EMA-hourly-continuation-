# EMA Hourly Continuation — KAVA/USDT P20_50

**Symbol:** KAVA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.6303 |
| net_win_rate | 0.4602 |
| gross_profit_factor | 0.9410 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -4.3358 |
| sortino_ratio | -1.4883 |
| max_drawdown | 0.8323 |
| cagr | -0.5003 |
| net_avg_win | 52.8672 |
| net_avg_loss | -71.5115 |
| avg_hold_time_bars | 8.1488 |
| exposure | 0.2141 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
