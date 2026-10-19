# EMA Hourly Continuation — ATOM/USDT P12_50

**Symbol:** ATOM/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1009 |
| net_profit_factor | 0.4683 |
| net_win_rate | 0.4579 |
| gross_profit_factor | 0.8740 |
| gross_win_rate | 0.4718 |
| sharpe_ratio | -6.8154 |
| sortino_ratio | -3.0513 |
| max_drawdown | 0.9764 |
| cagr | -0.7732 |
| net_avg_win | 18.6012 |
| net_avg_loss | -33.5517 |
| avg_hold_time_bars | 7.4202 |
| exposure | 0.3403 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
