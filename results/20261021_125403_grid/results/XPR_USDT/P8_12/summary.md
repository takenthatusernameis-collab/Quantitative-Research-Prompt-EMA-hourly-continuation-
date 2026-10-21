# EMA Hourly Continuation — XPR/USDT P8_12

**Symbol:** XPR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 143 |
| net_profit_factor | 0.6057 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8384 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -1.9052 |
| sortino_ratio | -0.3250 |
| max_drawdown | 0.3319 |
| cagr | -0.1393 |
| net_avg_win | 74.1860 |
| net_avg_loss | -102.0619 |
| avg_hold_time_bars | 13.1259 |
| exposure | 0.0853 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
