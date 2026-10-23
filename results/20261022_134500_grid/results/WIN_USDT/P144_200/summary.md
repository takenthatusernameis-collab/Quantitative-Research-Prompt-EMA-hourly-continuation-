# EMA Hourly Continuation — WIN/USDT P144_200

**Symbol:** WIN/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.2147 |
| net_win_rate | 0.3622 |
| gross_profit_factor | 0.6020 |
| gross_win_rate | 0.3885 |
| sharpe_ratio | -7.5555 |
| sortino_ratio | -2.1390 |
| max_drawdown | 0.9390 |
| cagr | -0.6717 |
| net_avg_win | 18.5989 |
| net_avg_loss | -49.2051 |
| avg_hold_time_bars | 5.0735 |
| exposure | 0.0879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
