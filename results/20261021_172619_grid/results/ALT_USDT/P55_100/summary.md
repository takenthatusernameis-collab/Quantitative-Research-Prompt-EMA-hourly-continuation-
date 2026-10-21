# EMA Hourly Continuation — ALT/USDT P55_100

**Symbol:** ALT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.7125 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9426 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -1.9391 |
| sortino_ratio | -0.5438 |
| max_drawdown | 0.4745 |
| cagr | -0.2203 |
| net_avg_win | 60.9338 |
| net_avg_loss | -82.8925 |
| avg_hold_time_bars | 9.0260 |
| exposure | 0.1575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
