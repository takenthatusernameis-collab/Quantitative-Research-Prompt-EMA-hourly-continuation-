# EMA Hourly Continuation — G/USDT P12_26

**Symbol:** G/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1058 |
| net_profit_factor | 0.3852 |
| net_win_rate | 0.4329 |
| gross_profit_factor | 0.8249 |
| gross_win_rate | 0.4584 |
| sharpe_ratio | -9.6606 |
| sortino_ratio | -4.8017 |
| max_drawdown | 0.9940 |
| cagr | -0.9053 |
| net_avg_win | 13.5974 |
| net_avg_loss | -26.9461 |
| avg_hold_time_bars | 4.1758 |
| exposure | 0.2323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
