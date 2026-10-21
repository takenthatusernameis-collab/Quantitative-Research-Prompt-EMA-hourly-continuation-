# EMA Hourly Continuation — JTO/USDT P8_34

**Symbol:** JTO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 773 |
| net_profit_factor | 0.7847 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 0.9843 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -2.3208 |
| sortino_ratio | -0.9224 |
| max_drawdown | 0.6879 |
| cagr | -0.3465 |
| net_avg_win | 63.1117 |
| net_avg_loss | -77.3692 |
| avg_hold_time_bars | 9.3312 |
| exposure | 0.3279 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
