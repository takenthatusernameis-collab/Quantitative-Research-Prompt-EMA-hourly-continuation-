# EMA Hourly Continuation — LINK/USDT P12_100

**Symbol:** LINK/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.8336 |
| net_win_rate | 0.5058 |
| gross_profit_factor | 1.0388 |
| gross_win_rate | 0.5058 |
| sharpe_ratio | -1.3012 |
| sortino_ratio | -0.3873 |
| max_drawdown | 0.4128 |
| cagr | -0.1647 |
| net_avg_win | 83.5815 |
| net_avg_loss | -102.6181 |
| avg_hold_time_bars | 28.1114 |
| exposure | 0.5507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
