# EMA Hourly Continuation — CFX/USDT P26_144

**Symbol:** CFX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.8683 |
| net_win_rate | 0.5179 |
| gross_profit_factor | 1.0644 |
| gross_win_rate | 0.5179 |
| sharpe_ratio | -0.8219 |
| sortino_ratio | -0.2249 |
| max_drawdown | 0.2782 |
| cagr | -0.1005 |
| net_avg_win | 81.9393 |
| net_avg_loss | -101.3729 |
| avg_hold_time_bars | 27.6667 |
| exposure | 0.4565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
