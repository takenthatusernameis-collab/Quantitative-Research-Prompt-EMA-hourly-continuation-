# EMA Hourly Continuation — XNO/USDT P50_55

**Symbol:** XNO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 138 |
| net_profit_factor | 0.5580 |
| net_win_rate | 0.4420 |
| gross_profit_factor | 0.7918 |
| gross_win_rate | 0.4420 |
| sharpe_ratio | -2.0980 |
| sortino_ratio | -0.3515 |
| max_drawdown | 0.3439 |
| cagr | -0.1485 |
| net_avg_win | 68.7546 |
| net_avg_loss | -97.6175 |
| avg_hold_time_bars | 5.0725 |
| exposure | 0.0318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
