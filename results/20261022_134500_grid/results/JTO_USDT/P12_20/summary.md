# EMA Hourly Continuation — JTO/USDT P12_20

**Symbol:** JTO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1510 |
| net_profit_factor | 0.3811 |
| net_win_rate | 0.4265 |
| gross_profit_factor | 0.8456 |
| gross_win_rate | 0.4530 |
| sharpe_ratio | -11.1984 |
| sortino_ratio | -6.1497 |
| max_drawdown | 0.9996 |
| cagr | -0.9537 |
| net_avg_win | 9.5565 |
| net_avg_loss | -18.6489 |
| avg_hold_time_bars | 2.4066 |
| exposure | 0.1652 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
