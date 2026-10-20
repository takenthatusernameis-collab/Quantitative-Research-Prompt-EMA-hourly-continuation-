# EMA Hourly Continuation — RPL/USDT P8_21

**Symbol:** RPL/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1413 |
| net_profit_factor | 0.4925 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 1.0120 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -8.1499 |
| sortino_ratio | -4.2953 |
| max_drawdown | 0.9951 |
| cagr | -0.8790 |
| net_avg_win | 14.7230 |
| net_avg_loss | -25.9045 |
| avg_hold_time_bars | 4.1741 |
| exposure | 0.2669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
