# EMA Hourly Continuation — BAT/USDT P20_200

**Symbol:** BAT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.8068 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 1.0005 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -1.1652 |
| sortino_ratio | -0.3105 |
| max_drawdown | 0.3910 |
| cagr | -0.1339 |
| net_avg_win | 72.3238 |
| net_avg_loss | -91.2091 |
| avg_hold_time_bars | 38.5447 |
| exposure | 0.6080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
