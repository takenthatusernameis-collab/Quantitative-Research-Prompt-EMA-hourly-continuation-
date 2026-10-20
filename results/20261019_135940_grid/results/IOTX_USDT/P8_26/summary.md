# EMA Hourly Continuation — IOTX/USDT P8_26

**Symbol:** IOTX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1493 |
| net_profit_factor | 0.5307 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.9881 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -8.9040 |
| sortino_ratio | -4.8772 |
| max_drawdown | 0.9974 |
| cagr | -0.9053 |
| net_avg_win | 16.2766 |
| net_avg_loss | -26.5660 |
| avg_hold_time_bars | 4.1875 |
| exposure | 0.2842 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
