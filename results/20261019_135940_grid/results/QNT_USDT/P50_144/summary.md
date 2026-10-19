# EMA Hourly Continuation — QNT/USDT P50_144

**Symbol:** QNT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 619 |
| net_profit_factor | 0.5505 |
| net_win_rate | 0.4733 |
| gross_profit_factor | 0.9198 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -4.5616 |
| sortino_ratio | -1.6031 |
| max_drawdown | 0.8584 |
| cagr | -0.5346 |
| net_avg_win | 35.6807 |
| net_avg_loss | -58.2512 |
| avg_hold_time_bars | 9.0679 |
| exposure | 0.2551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
