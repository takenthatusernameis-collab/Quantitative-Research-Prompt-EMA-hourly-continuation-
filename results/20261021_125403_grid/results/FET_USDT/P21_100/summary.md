# EMA Hourly Continuation — FET/USDT P21_100

**Symbol:** FET/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.8478 |
| net_win_rate | 0.5012 |
| gross_profit_factor | 1.0028 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -1.0059 |
| sortino_ratio | -0.2892 |
| max_drawdown | 0.3285 |
| cagr | -0.1268 |
| net_avg_win | 79.5837 |
| net_avg_loss | -94.3354 |
| avg_hold_time_bars | 23.2556 |
| exposure | 0.4260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
