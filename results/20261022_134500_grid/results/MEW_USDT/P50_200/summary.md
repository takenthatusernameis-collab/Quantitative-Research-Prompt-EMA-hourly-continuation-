# EMA Hourly Continuation — MEW/USDT P50_200

**Symbol:** MEW/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.6707 |
| net_win_rate | 0.4673 |
| gross_profit_factor | 0.8902 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -2.3255 |
| sortino_ratio | -0.5978 |
| max_drawdown | 0.5494 |
| cagr | -0.2482 |
| net_avg_win | 66.3750 |
| net_avg_loss | -86.7960 |
| avg_hold_time_bars | 29.5923 |
| exposure | 0.4520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
