# EMA Hourly Continuation — MANTA/USDT P8_50

**Symbol:** MANTA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 986 |
| net_profit_factor | 0.6363 |
| net_win_rate | 0.4584 |
| gross_profit_factor | 0.9570 |
| gross_win_rate | 0.4645 |
| sharpe_ratio | -5.3895 |
| sortino_ratio | -2.3904 |
| max_drawdown | 0.9424 |
| cagr | -0.6778 |
| net_avg_win | 36.4585 |
| net_avg_loss | -48.4975 |
| avg_hold_time_bars | 12.1795 |
| exposure | 0.5459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
