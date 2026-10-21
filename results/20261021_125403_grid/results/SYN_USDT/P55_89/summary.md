# EMA Hourly Continuation — SYN/USDT P55_89

**Symbol:** SYN/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.8610 |
| net_win_rate | 0.5309 |
| gross_profit_factor | 1.1338 |
| gross_win_rate | 0.5309 |
| sharpe_ratio | -0.8989 |
| sortino_ratio | -0.2449 |
| max_drawdown | 0.3297 |
| cagr | -0.1079 |
| net_avg_win | 81.6823 |
| net_avg_loss | -107.3685 |
| avg_hold_time_bars | 7.2303 |
| exposure | 0.1170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
