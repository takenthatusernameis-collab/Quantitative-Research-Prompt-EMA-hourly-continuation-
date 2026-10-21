# EMA Hourly Continuation — 1INCH/USDT P8_21

**Symbol:** 1INCH/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.6195 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.9091 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -3.8455 |
| sortino_ratio | -1.3616 |
| max_drawdown | 0.7953 |
| cagr | -0.4638 |
| net_avg_win | 44.2471 |
| net_avg_loss | -65.3620 |
| avg_hold_time_bars | 5.5944 |
| exposure | 0.1549 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
