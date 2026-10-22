# EMA Hourly Continuation — TRAC/USDT P8_26

**Symbol:** TRAC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1251 |
| net_profit_factor | 0.4708 |
| net_win_rate | 0.4380 |
| gross_profit_factor | 0.8902 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -8.6927 |
| sortino_ratio | -4.3103 |
| max_drawdown | 0.9954 |
| cagr | -0.8822 |
| net_avg_win | 16.1583 |
| net_avg_loss | -26.7543 |
| avg_hold_time_bars | 5.1175 |
| exposure | 0.2910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
