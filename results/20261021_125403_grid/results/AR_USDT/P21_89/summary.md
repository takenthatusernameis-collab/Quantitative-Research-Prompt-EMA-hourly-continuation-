# EMA Hourly Continuation — AR/USDT P21_89

**Symbol:** AR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.7493 |
| net_win_rate | 0.4830 |
| gross_profit_factor | 0.9118 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -1.9103 |
| sortino_ratio | -0.6098 |
| max_drawdown | 0.5380 |
| cagr | -0.2457 |
| net_avg_win | 62.6612 |
| net_avg_loss | -78.1390 |
| avg_hold_time_bars | 14.5050 |
| exposure | 0.3303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
