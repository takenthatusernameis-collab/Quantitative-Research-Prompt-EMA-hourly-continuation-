# EMA Hourly Continuation — SSV/USDT P8_50

**Symbol:** SSV/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1105 |
| net_profit_factor | 0.6386 |
| net_win_rate | 0.4534 |
| gross_profit_factor | 0.9522 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -6.1720 |
| sortino_ratio | -2.8827 |
| max_drawdown | 0.9706 |
| cagr | -0.7473 |
| net_avg_win | 34.1786 |
| net_avg_loss | -44.3915 |
| avg_hold_time_bars | 10.0570 |
| exposure | 0.5029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
