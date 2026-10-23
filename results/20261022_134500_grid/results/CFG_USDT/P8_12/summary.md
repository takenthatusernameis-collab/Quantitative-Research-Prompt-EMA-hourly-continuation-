# EMA Hourly Continuation — CFG/USDT P8_12

**Symbol:** CFG/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1897 |
| net_profit_factor | 0.1351 |
| net_win_rate | 0.3363 |
| gross_profit_factor | 0.4850 |
| gross_win_rate | 0.3743 |
| sharpe_ratio | -18.2589 |
| sortino_ratio | -11.4085 |
| max_drawdown | 1.0000 |
| cagr | -0.9974 |
| net_avg_win | 2.4485 |
| net_avg_loss | -9.1836 |
| avg_hold_time_bars | 1.8830 |
| exposure | 0.1624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
