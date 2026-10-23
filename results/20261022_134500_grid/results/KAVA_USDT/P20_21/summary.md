# EMA Hourly Continuation — KAVA/USDT P20_21

**Symbol:** KAVA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1289 |
| net_profit_factor | 0.1111 |
| net_win_rate | 0.2708 |
| gross_profit_factor | 0.5753 |
| gross_win_rate | 0.3770 |
| sharpe_ratio | -19.7474 |
| sortino_ratio | -11.1001 |
| max_drawdown | 1.0000 |
| cagr | -0.9980 |
| net_avg_win | 3.5814 |
| net_avg_loss | -11.9680 |
| avg_hold_time_bars | 2.2428 |
| exposure | 0.1314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
