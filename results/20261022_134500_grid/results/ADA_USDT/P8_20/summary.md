# EMA Hourly Continuation — ADA/USDT P8_20

**Symbol:** ADA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1712 |
| net_profit_factor | 0.2858 |
| net_win_rate | 0.4060 |
| gross_profit_factor | 0.8598 |
| gross_win_rate | 0.4317 |
| sharpe_ratio | -14.5291 |
| sortino_ratio | -8.5068 |
| max_drawdown | 1.0000 |
| cagr | -0.9886 |
| net_avg_win | 5.7576 |
| net_avg_loss | -13.7673 |
| avg_hold_time_bars | 2.4907 |
| exposure | 0.1938 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
