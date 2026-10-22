# EMA Hourly Continuation — DASH/USDT P50_55

**Symbol:** DASH/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 846 |
| net_profit_factor | 0.1317 |
| net_win_rate | 0.3061 |
| gross_profit_factor | 0.7594 |
| gross_win_rate | 0.3853 |
| sharpe_ratio | -13.9865 |
| sortino_ratio | -6.0852 |
| max_drawdown | 0.9998 |
| cagr | -0.9649 |
| net_avg_win | 5.8574 |
| net_avg_loss | -19.6164 |
| avg_hold_time_bars | 1.6785 |
| exposure | 0.0645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
