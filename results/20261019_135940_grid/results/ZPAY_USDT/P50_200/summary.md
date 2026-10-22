# EMA Hourly Continuation — ZPAY/USDT P50_200

**Symbol:** ZPAY/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.5643 |
| net_win_rate | 0.4093 |
| gross_profit_factor | 0.6981 |
| gross_win_rate | 0.4118 |
| sharpe_ratio | -3.4110 |
| sortino_ratio | -0.9634 |
| max_drawdown | 0.6860 |
| cagr | -0.3603 |
| net_avg_win | 52.4311 |
| net_avg_loss | -64.3828 |
| avg_hold_time_bars | 26.2623 |
| exposure | 0.4849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
