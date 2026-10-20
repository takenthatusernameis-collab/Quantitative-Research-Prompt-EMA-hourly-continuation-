# EMA Hourly Continuation — TFUEL/USDT P20_26

**Symbol:** TFUEL/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1328 |
| net_profit_factor | 0.2564 |
| net_win_rate | 0.3200 |
| gross_profit_factor | 0.7622 |
| gross_win_rate | 0.3878 |
| sharpe_ratio | -16.7798 |
| sortino_ratio | -8.9986 |
| max_drawdown | 1.0000 |
| cagr | -0.9920 |
| net_avg_win | 8.1135 |
| net_avg_loss | -14.8928 |
| avg_hold_time_bars | 2.3095 |
| exposure | 0.1388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
