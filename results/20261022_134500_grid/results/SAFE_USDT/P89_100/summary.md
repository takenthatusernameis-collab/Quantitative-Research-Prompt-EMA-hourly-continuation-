# EMA Hourly Continuation — SAFE/USDT P89_100

**Symbol:** SAFE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 576 |
| net_profit_factor | 0.2128 |
| net_win_rate | 0.3715 |
| gross_profit_factor | 0.5626 |
| gross_win_rate | 0.4010 |
| sharpe_ratio | -9.3658 |
| sortino_ratio | -3.2490 |
| max_drawdown | 0.9871 |
| cagr | -0.8228 |
| net_avg_win | 12.4594 |
| net_avg_loss | -34.6200 |
| avg_hold_time_bars | 3.2778 |
| exposure | 0.0865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
