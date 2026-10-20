# EMA Hourly Continuation — PEOPLE/USDT P8_26

**Symbol:** PEOPLE/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1480 |
| net_profit_factor | 0.4411 |
| net_win_rate | 0.4345 |
| gross_profit_factor | 0.7508 |
| gross_win_rate | 0.4459 |
| sharpe_ratio | -9.0397 |
| sortino_ratio | -4.8822 |
| max_drawdown | 0.9975 |
| cagr | -0.9071 |
| net_avg_win | 12.2434 |
| net_avg_loss | -21.3233 |
| avg_hold_time_bars | 4.3108 |
| exposure | 0.2887 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
