# EMA Hourly Continuation — TRX/USDT P8_12

**Symbol:** TRX/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1576 |
| net_profit_factor | 0.0262 |
| net_win_rate | 0.1726 |
| gross_profit_factor | 0.5879 |
| gross_win_rate | 0.3718 |
| sharpe_ratio | -26.8612 |
| sortino_ratio | -19.2936 |
| max_drawdown | 1.0000 |
| cagr | -1.0000 |
| net_avg_win | 0.9899 |
| net_avg_loss | -7.8752 |
| avg_hold_time_bars | 2.0914 |
| exposure | 0.1498 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
