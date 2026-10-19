# EMA Hourly Continuation — CRO/USDT P12_50

**Symbol:** CRO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1103 |
| net_profit_factor | 0.3965 |
| net_win_rate | 0.4288 |
| gross_profit_factor | 0.8675 |
| gross_win_rate | 0.4560 |
| sharpe_ratio | -9.1315 |
| sortino_ratio | -4.2715 |
| max_drawdown | 0.9957 |
| cagr | -0.8826 |
| net_avg_win | 13.8285 |
| net_avg_loss | -26.1821 |
| avg_hold_time_bars | 7.0045 |
| exposure | 0.3512 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
