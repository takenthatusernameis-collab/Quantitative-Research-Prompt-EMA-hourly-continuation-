# EMA Hourly Continuation — RAY/USDT P12_21

**Symbol:** RAY/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1445 |
| net_profit_factor | 0.4094 |
| net_win_rate | 0.4042 |
| gross_profit_factor | 0.9088 |
| gross_win_rate | 0.4311 |
| sharpe_ratio | -12.0622 |
| sortino_ratio | -6.5119 |
| max_drawdown | 0.9997 |
| cagr | -0.9622 |
| net_avg_win | 11.8685 |
| net_avg_loss | -19.6615 |
| avg_hold_time_bars | 2.3862 |
| exposure | 0.1567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
