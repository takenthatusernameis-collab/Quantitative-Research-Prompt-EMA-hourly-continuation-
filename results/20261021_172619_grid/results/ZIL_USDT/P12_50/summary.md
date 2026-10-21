# EMA Hourly Continuation — ZIL/USDT P12_50

**Symbol:** ZIL/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 619 |
| net_profit_factor | 0.7276 |
| net_win_rate | 0.4895 |
| gross_profit_factor | 0.9775 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -2.6386 |
| sortino_ratio | -0.9398 |
| max_drawdown | 0.6975 |
| cagr | -0.3506 |
| net_avg_win | 58.3466 |
| net_avg_loss | -76.8903 |
| avg_hold_time_bars | 11.7092 |
| exposure | 0.3295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
