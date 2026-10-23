# EMA Hourly Continuation — CSPR/USDT P50_200

**Symbol:** CSPR/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 591 |
| net_profit_factor | 0.4919 |
| net_win_rate | 0.3976 |
| gross_profit_factor | 0.7431 |
| gross_win_rate | 0.3993 |
| sharpe_ratio | -5.8920 |
| sortino_ratio | -2.0065 |
| max_drawdown | 0.9143 |
| cagr | -0.6228 |
| net_avg_win | 37.6294 |
| net_avg_loss | -50.5016 |
| avg_hold_time_bars | 14.4636 |
| exposure | 0.3885 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
