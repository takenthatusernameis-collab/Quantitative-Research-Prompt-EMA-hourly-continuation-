# EMA Hourly Continuation — ETC/USDT P12_50

**Symbol:** ETC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1137 |
| net_profit_factor | 0.4947 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.9669 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -8.3535 |
| sortino_ratio | -3.9699 |
| max_drawdown | 0.9928 |
| cagr | -0.8591 |
| net_avg_win | 18.7605 |
| net_avg_loss | -31.7367 |
| avg_hold_time_bars | 6.0220 |
| exposure | 0.3112 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
