# EMA Hourly Continuation — MANTA/USDT P26_34

**Symbol:** MANTA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1062 |
| net_profit_factor | 0.4056 |
| net_win_rate | 0.3974 |
| gross_profit_factor | 1.0156 |
| gross_win_rate | 0.4275 |
| sharpe_ratio | -11.5263 |
| sortino_ratio | -5.3505 |
| max_drawdown | 0.9991 |
| cagr | -0.9393 |
| net_avg_win | 16.1585 |
| net_avg_loss | -26.2658 |
| avg_hold_time_bars | 2.3776 |
| exposure | 0.1148 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
