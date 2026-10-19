# EMA Hourly Continuation — JTO/USDT P50_200

**Symbol:** JTO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.6144 |
| net_win_rate | 0.4496 |
| gross_profit_factor | 0.8358 |
| gross_win_rate | 0.4570 |
| sharpe_ratio | -2.9627 |
| sortino_ratio | -0.8438 |
| max_drawdown | 0.6456 |
| cagr | -0.3247 |
| net_avg_win | 54.5915 |
| net_avg_loss | -72.5842 |
| avg_hold_time_bars | 19.2187 |
| exposure | 0.3555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
