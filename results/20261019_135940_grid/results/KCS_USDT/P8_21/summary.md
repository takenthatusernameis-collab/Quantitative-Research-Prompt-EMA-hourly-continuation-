# EMA Hourly Continuation — KCS/USDT P8_21

**Symbol:** KCS/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1586 |
| net_profit_factor | 0.1453 |
| net_win_rate | 0.2938 |
| gross_profit_factor | 0.6680 |
| gross_win_rate | 0.3726 |
| sharpe_ratio | -20.9961 |
| sortino_ratio | -12.7285 |
| max_drawdown | 1.0000 |
| cagr | -0.9992 |
| net_avg_win | 3.6470 |
| net_avg_loss | -10.4460 |
| avg_hold_time_bars | 3.6564 |
| exposure | 0.2636 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
