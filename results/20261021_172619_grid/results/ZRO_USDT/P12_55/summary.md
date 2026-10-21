# EMA Hourly Continuation — ZRO/USDT P12_55

**Symbol:** ZRO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.9597 |
| net_win_rate | 0.5406 |
| gross_profit_factor | 1.1609 |
| gross_win_rate | 0.5406 |
| sharpe_ratio | -0.2207 |
| sortino_ratio | -0.0789 |
| max_drawdown | 0.2951 |
| cagr | -0.0455 |
| net_avg_win | 80.0587 |
| net_avg_loss | -98.1781 |
| avg_hold_time_bars | 13.0830 |
| exposure | 0.3624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
