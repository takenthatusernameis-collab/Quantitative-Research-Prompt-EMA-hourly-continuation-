# EMA Hourly Continuation — WIN/USDT P12_26

**Symbol:** WIN/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.6473 |
| net_win_rate | 0.5111 |
| gross_profit_factor | 1.0505 |
| gross_win_rate | 0.5111 |
| sharpe_ratio | -2.7086 |
| sortino_ratio | -0.7898 |
| max_drawdown | 0.5980 |
| cagr | -0.3013 |
| net_avg_win | 52.3775 |
| net_avg_loss | -84.5783 |
| avg_hold_time_bars | 6.6732 |
| exposure | 0.1235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
