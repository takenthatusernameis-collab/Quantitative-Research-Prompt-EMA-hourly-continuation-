# EMA Hourly Continuation — UNI/USDT P144_200

**Symbol:** UNI/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.4133 |
| net_win_rate | 0.4200 |
| gross_profit_factor | 0.7663 |
| gross_win_rate | 0.4300 |
| sharpe_ratio | -5.4370 |
| sortino_ratio | -1.5356 |
| max_drawdown | 0.8564 |
| cagr | -0.5333 |
| net_avg_win | 35.7483 |
| net_avg_loss | -62.6312 |
| avg_hold_time_bars | 4.2450 |
| exposure | 0.0772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
