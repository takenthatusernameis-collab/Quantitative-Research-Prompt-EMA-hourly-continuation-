# EMA Hourly Continuation — MASK/USDT P12_20

**Symbol:** MASK/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1489 |
| net_profit_factor | 0.2001 |
| net_win_rate | 0.3915 |
| gross_profit_factor | 0.6519 |
| gross_win_rate | 0.4453 |
| sharpe_ratio | -14.4325 |
| sortino_ratio | -7.9785 |
| max_drawdown | 1.0000 |
| cagr | -0.9850 |
| net_avg_win | 4.2912 |
| net_avg_loss | -13.7986 |
| avg_hold_time_bars | 2.6555 |
| exposure | 0.1797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
