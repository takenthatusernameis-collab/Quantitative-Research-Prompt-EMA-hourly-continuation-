# EMA Hourly Continuation — QI/USDT P8_12

**Symbol:** QI/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1538 |
| net_profit_factor | 0.2849 |
| net_win_rate | 0.3882 |
| gross_profit_factor | 0.7771 |
| gross_win_rate | 0.4402 |
| sharpe_ratio | -14.7240 |
| sortino_ratio | -8.2681 |
| max_drawdown | 1.0000 |
| cagr | -0.9871 |
| net_avg_win | 6.6727 |
| net_avg_loss | -14.8602 |
| avg_hold_time_bars | 2.6912 |
| exposure | 0.1873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
