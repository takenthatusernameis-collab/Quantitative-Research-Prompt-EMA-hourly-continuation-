# EMA Hourly Continuation — BDX/USDT P12_100

**Symbol:** BDX/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.5444 |
| net_win_rate | 0.4407 |
| gross_profit_factor | 0.8307 |
| gross_win_rate | 0.4427 |
| sharpe_ratio | -4.6459 |
| sortino_ratio | -1.4894 |
| max_drawdown | 0.8315 |
| cagr | -0.5000 |
| net_avg_win | 44.1905 |
| net_avg_loss | -63.9594 |
| avg_hold_time_bars | 14.5415 |
| exposure | 0.3345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
