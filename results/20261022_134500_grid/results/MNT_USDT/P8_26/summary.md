# EMA Hourly Continuation — MNT/USDT P8_26

**Symbol:** MNT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1515 |
| net_profit_factor | 0.2995 |
| net_win_rate | 0.4040 |
| gross_profit_factor | 0.7288 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -12.6784 |
| sortino_ratio | -6.9863 |
| max_drawdown | 0.9999 |
| cagr | -0.9723 |
| net_avg_win | 6.9847 |
| net_avg_loss | -15.8066 |
| avg_hold_time_bars | 4.5881 |
| exposure | 0.3160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
