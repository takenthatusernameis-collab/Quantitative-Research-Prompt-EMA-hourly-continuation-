# EMA Hourly Continuation — ONE/USDT P12_21

**Symbol:** ONE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.8672 |
| net_win_rate | 0.5401 |
| gross_profit_factor | 1.1706 |
| gross_win_rate | 0.5436 |
| sharpe_ratio | -0.6905 |
| sortino_ratio | -0.1694 |
| max_drawdown | 0.2469 |
| cagr | -0.0765 |
| net_avg_win | 76.3402 |
| net_avg_loss | -103.3643 |
| avg_hold_time_bars | 4.6794 |
| exposure | 0.0610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
