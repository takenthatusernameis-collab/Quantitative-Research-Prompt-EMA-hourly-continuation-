# EMA Hourly Continuation — PUFFER/USDT P12_26

**Symbol:** PUFFER/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.7001 |
| net_win_rate | 0.4798 |
| gross_profit_factor | 0.9298 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -2.7052 |
| sortino_ratio | -0.8843 |
| max_drawdown | 0.5977 |
| cagr | -0.3344 |
| net_avg_win | 64.7304 |
| net_avg_loss | -85.2785 |
| avg_hold_time_bars | 6.1710 |
| exposure | 0.1470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
