# EMA Hourly Continuation — MNT/USDT P20_144

**Symbol:** MNT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.5788 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9473 |
| gross_win_rate | 0.4966 |
| sharpe_ratio | -3.0462 |
| sortino_ratio | -0.8877 |
| max_drawdown | 0.6946 |
| cagr | -0.3540 |
| net_avg_win | 43.1806 |
| net_avg_loss | -70.2966 |
| avg_hold_time_bars | 29.5103 |
| exposure | 0.5862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
