# EMA Hourly Continuation — INJ/USDT P100_200

**Symbol:** INJ/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.4766 |
| net_win_rate | 0.4236 |
| gross_profit_factor | 0.7116 |
| gross_win_rate | 0.4286 |
| sharpe_ratio | -4.4032 |
| sortino_ratio | -1.2478 |
| max_drawdown | 0.7872 |
| cagr | -0.4537 |
| net_avg_win | 41.3503 |
| net_avg_loss | -63.7683 |
| avg_hold_time_bars | 9.0222 |
| exposure | 0.1665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
