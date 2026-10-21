# EMA Hourly Continuation — AKT/USDT P55_89

**Symbol:** AKT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.9230 |
| net_win_rate | 0.5470 |
| gross_profit_factor | 1.1974 |
| gross_win_rate | 0.5470 |
| sharpe_ratio | -0.3793 |
| sortino_ratio | -0.0932 |
| max_drawdown | 0.1633 |
| cagr | -0.0452 |
| net_avg_win | 83.7510 |
| net_avg_loss | -109.5836 |
| avg_hold_time_bars | 7.4425 |
| exposure | 0.0971 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
