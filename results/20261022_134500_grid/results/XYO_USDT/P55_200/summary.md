# EMA Hourly Continuation — XYO/USDT P55_200

**Symbol:** XYO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.5120 |
| net_win_rate | 0.4397 |
| gross_profit_factor | 0.7872 |
| gross_win_rate | 0.4499 |
| sharpe_ratio | -4.5171 |
| sortino_ratio | -1.4057 |
| max_drawdown | 0.8218 |
| cagr | -0.4879 |
| net_avg_win | 39.7811 |
| net_avg_loss | -60.9666 |
| avg_hold_time_bars | 16.3742 |
| exposure | 0.3623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
