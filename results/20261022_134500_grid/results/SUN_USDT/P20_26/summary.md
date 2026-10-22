# EMA Hourly Continuation — SUN/USDT P20_26

**Symbol:** SUN/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1079 |
| net_profit_factor | 0.0818 |
| net_win_rate | 0.2669 |
| gross_profit_factor | 0.5551 |
| gross_win_rate | 0.4069 |
| sharpe_ratio | -17.8097 |
| sortino_ratio | -9.1975 |
| max_drawdown | 1.0000 |
| cagr | -0.9933 |
| net_avg_win | 3.0913 |
| net_avg_loss | -13.7677 |
| avg_hold_time_bars | 2.9611 |
| exposure | 0.1446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
