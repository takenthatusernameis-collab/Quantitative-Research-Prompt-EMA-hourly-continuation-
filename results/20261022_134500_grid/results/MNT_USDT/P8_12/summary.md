# EMA Hourly Continuation — MNT/USDT P8_12

**Symbol:** MNT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1894 |
| net_profit_factor | 0.1269 |
| net_win_rate | 0.3200 |
| gross_profit_factor | 0.5616 |
| gross_win_rate | 0.4124 |
| sharpe_ratio | -21.1709 |
| sortino_ratio | -13.7447 |
| max_drawdown | 1.0000 |
| cagr | -0.9994 |
| net_avg_win | 2.3976 |
| net_avg_loss | -8.8921 |
| avg_hold_time_bars | 2.0137 |
| exposure | 0.1734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
