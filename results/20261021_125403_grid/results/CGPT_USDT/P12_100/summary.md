# EMA Hourly Continuation — CGPT/USDT P12_100

**Symbol:** CGPT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.8443 |
| net_win_rate | 0.5022 |
| gross_profit_factor | 1.0152 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -1.1854 |
| sortino_ratio | -0.3585 |
| max_drawdown | 0.3831 |
| cagr | -0.1541 |
| net_avg_win | 83.0569 |
| net_avg_loss | -99.2638 |
| avg_hold_time_bars | 28.2309 |
| exposure | 0.5723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
