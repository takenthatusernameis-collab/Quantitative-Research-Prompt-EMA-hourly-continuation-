# EMA Hourly Continuation — T/USDT P20_55

**Symbol:** T/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.6947 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 1.0426 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -3.0629 |
| sortino_ratio | -1.0513 |
| max_drawdown | 0.7249 |
| cagr | -0.3836 |
| net_avg_win | 55.3028 |
| net_avg_loss | -80.1637 |
| avg_hold_time_bars | 9.4083 |
| exposure | 0.2461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
