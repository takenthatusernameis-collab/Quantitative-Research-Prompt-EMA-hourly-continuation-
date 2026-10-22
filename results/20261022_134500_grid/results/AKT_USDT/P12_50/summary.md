# EMA Hourly Continuation — AKT/USDT P12_50

**Symbol:** AKT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1090 |
| net_profit_factor | 0.5018 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.8335 |
| gross_win_rate | 0.4560 |
| sharpe_ratio | -6.7861 |
| sortino_ratio | -3.1393 |
| max_drawdown | 0.9800 |
| cagr | -0.7835 |
| net_avg_win | 20.0753 |
| net_avg_loss | -32.7925 |
| avg_hold_time_bars | 6.4303 |
| exposure | 0.3186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
