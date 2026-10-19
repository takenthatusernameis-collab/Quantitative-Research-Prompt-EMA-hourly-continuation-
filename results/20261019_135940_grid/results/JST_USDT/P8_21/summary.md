# EMA Hourly Continuation — JST/USDT P8_21

**Symbol:** JST/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1355 |
| net_profit_factor | 0.1390 |
| net_win_rate | 0.3815 |
| gross_profit_factor | 0.6634 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -15.2597 |
| sortino_ratio | -8.1694 |
| max_drawdown | 1.0000 |
| cagr | -0.9878 |
| net_avg_win | 3.1218 |
| net_avg_loss | -13.8590 |
| avg_hold_time_bars | 3.8856 |
| exposure | 0.2382 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
