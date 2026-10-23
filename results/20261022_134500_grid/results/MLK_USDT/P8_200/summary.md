# EMA Hourly Continuation — MLK/USDT P8_200

**Symbol:** MLK/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 732 |
| net_profit_factor | 0.4401 |
| net_win_rate | 0.3620 |
| gross_profit_factor | 0.6702 |
| gross_win_rate | 0.3702 |
| sharpe_ratio | -7.9746 |
| sortino_ratio | -3.0197 |
| max_drawdown | 0.9772 |
| cagr | -0.7748 |
| net_avg_win | 28.9764 |
| net_avg_loss | -37.3577 |
| avg_hold_time_bars | 20.6571 |
| exposure | 0.6843 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
