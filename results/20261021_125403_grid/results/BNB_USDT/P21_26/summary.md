# EMA Hourly Continuation — BNB/USDT P21_26

**Symbol:** BNB/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 122 |
| net_profit_factor | 0.6590 |
| net_win_rate | 0.5492 |
| gross_profit_factor | 1.2248 |
| gross_win_rate | 0.5492 |
| sharpe_ratio | -1.4234 |
| sortino_ratio | -0.2287 |
| max_drawdown | 0.2512 |
| cagr | -0.0990 |
| net_avg_win | 66.4244 |
| net_avg_loss | -122.7833 |
| avg_hold_time_bars | 6.0410 |
| exposure | 0.0335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
