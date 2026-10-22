# EMA Hourly Continuation — ETC/USDT P20_55

**Symbol:** ETC/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 969 |
| net_profit_factor | 0.3934 |
| net_win_rate | 0.4324 |
| gross_profit_factor | 0.8394 |
| gross_win_rate | 0.4603 |
| sharpe_ratio | -8.8220 |
| sortino_ratio | -3.8771 |
| max_drawdown | 0.9927 |
| cagr | -0.8582 |
| net_avg_win | 15.3655 |
| net_avg_loss | -29.7527 |
| avg_hold_time_bars | 5.4200 |
| exposure | 0.2387 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
