# EMA Hourly Continuation — TFUEL/USDT P100_144

**Symbol:** TFUEL/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.3548 |
| net_win_rate | 0.3706 |
| gross_profit_factor | 0.7385 |
| gross_win_rate | 0.3907 |
| sharpe_ratio | -8.9123 |
| sortino_ratio | -3.1203 |
| max_drawdown | 0.9831 |
| cagr | -0.8001 |
| net_avg_win | 24.3482 |
| net_avg_loss | -40.4060 |
| avg_hold_time_bars | 4.1586 |
| exposure | 0.1127 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
