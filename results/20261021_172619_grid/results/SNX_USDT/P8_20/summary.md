# EMA Hourly Continuation — SNX/USDT P8_20

**Symbol:** SNX/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 607 |
| net_profit_factor | 0.7792 |
| net_win_rate | 0.5206 |
| gross_profit_factor | 1.0918 |
| gross_win_rate | 0.5206 |
| sharpe_ratio | -2.0143 |
| sortino_ratio | -0.7144 |
| max_drawdown | 0.6069 |
| cagr | -0.2780 |
| net_avg_win | 62.5842 |
| net_avg_loss | -87.2141 |
| avg_hold_time_bars | 5.2850 |
| exposure | 0.1452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
