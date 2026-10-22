# EMA Hourly Continuation — ENA/USDT P21_50

**Symbol:** ENA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 970 |
| net_profit_factor | 0.5959 |
| net_win_rate | 0.4670 |
| gross_profit_factor | 0.8920 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -5.0941 |
| sortino_ratio | -2.2433 |
| max_drawdown | 0.9351 |
| cagr | -0.6545 |
| net_avg_win | 30.2943 |
| net_avg_loss | -44.5456 |
| avg_hold_time_bars | 4.6381 |
| exposure | 0.2045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
