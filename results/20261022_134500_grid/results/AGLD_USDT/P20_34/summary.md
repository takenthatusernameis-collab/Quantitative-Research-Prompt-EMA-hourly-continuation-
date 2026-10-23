# EMA Hourly Continuation — AGLD/USDT P20_34

**Symbol:** AGLD/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1120 |
| net_profit_factor | 0.4387 |
| net_win_rate | 0.4241 |
| gross_profit_factor | 0.8796 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -8.7190 |
| sortino_ratio | -4.1369 |
| max_drawdown | 0.9936 |
| cagr | -0.8648 |
| net_avg_win | 16.3469 |
| net_avg_loss | -27.4427 |
| avg_hold_time_bars | 3.5696 |
| exposure | 0.1809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
