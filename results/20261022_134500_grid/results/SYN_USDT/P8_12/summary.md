# EMA Hourly Continuation — SYN/USDT P8_12

**Symbol:** SYN/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1721 |
| net_profit_factor | 0.2885 |
| net_win_rate | 0.3899 |
| gross_profit_factor | 0.7568 |
| gross_win_rate | 0.4242 |
| sharpe_ratio | -14.3999 |
| sortino_ratio | -8.4766 |
| max_drawdown | 1.0000 |
| cagr | -0.9871 |
| net_avg_win | 6.0435 |
| net_avg_loss | -13.3857 |
| avg_hold_time_bars | 2.2098 |
| exposure | 0.1729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
