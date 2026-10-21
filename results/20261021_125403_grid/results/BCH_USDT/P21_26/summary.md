# EMA Hourly Continuation — BCH/USDT P21_26

**Symbol:** BCH/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 137 |
| net_profit_factor | 0.7245 |
| net_win_rate | 0.5255 |
| gross_profit_factor | 1.0946 |
| gross_win_rate | 0.5255 |
| sharpe_ratio | -1.1312 |
| sortino_ratio | -0.1913 |
| max_drawdown | 0.2370 |
| cagr | -0.0831 |
| net_avg_win | 71.4875 |
| net_avg_loss | -109.2971 |
| avg_hold_time_bars | 5.9708 |
| exposure | 0.0372 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
