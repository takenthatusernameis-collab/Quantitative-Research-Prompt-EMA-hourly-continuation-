# EMA Hourly Continuation — CTSI/USDT P144_200

**Symbol:** CTSI/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.4594 |
| net_win_rate | 0.4147 |
| gross_profit_factor | 0.8491 |
| gross_win_rate | 0.4332 |
| sharpe_ratio | -5.6494 |
| sortino_ratio | -1.6625 |
| max_drawdown | 0.8752 |
| cagr | -0.5626 |
| net_avg_win | 41.2909 |
| net_avg_loss | -63.6965 |
| avg_hold_time_bars | 4.3134 |
| exposure | 0.0851 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
