# EMA Hourly Continuation — AKT/USDT P21_144

**Symbol:** AKT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.9171 |
| net_win_rate | 0.5186 |
| gross_profit_factor | 1.0736 |
| gross_win_rate | 0.5186 |
| sharpe_ratio | -0.5101 |
| sortino_ratio | -0.1422 |
| max_drawdown | 0.2089 |
| cagr | -0.0677 |
| net_avg_win | 91.5563 |
| net_avg_loss | -107.5509 |
| avg_hold_time_bars | 28.9681 |
| exposure | 0.4951 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
