# EMA Hourly Continuation — ADA/USDT P144_200

**Symbol:** ADA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.4313 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.9682 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -5.0128 |
| sortino_ratio | -1.3459 |
| max_drawdown | 0.8271 |
| cagr | -0.5022 |
| net_avg_win | 36.8761 |
| net_avg_loss | -73.0364 |
| avg_hold_time_bars | 4.0108 |
| exposure | 0.0673 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
