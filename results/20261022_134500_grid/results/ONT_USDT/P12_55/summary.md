# EMA Hourly Continuation — ONT/USDT P12_55

**Symbol:** ONT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 998 |
| net_profit_factor | 0.5780 |
| net_win_rate | 0.4499 |
| gross_profit_factor | 0.9899 |
| gross_win_rate | 0.4669 |
| sharpe_ratio | -6.7164 |
| sortino_ratio | -2.9582 |
| max_drawdown | 0.9772 |
| cagr | -0.7685 |
| net_avg_win | 29.7404 |
| net_avg_loss | -42.0835 |
| avg_hold_time_bars | 8.1102 |
| exposure | 0.3663 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
