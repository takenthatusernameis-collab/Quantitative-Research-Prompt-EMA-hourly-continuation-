# EMA Hourly Continuation — BCH/USDT P50_89

**Symbol:** BCH/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.5889 |
| net_win_rate | 0.4671 |
| gross_profit_factor | 0.8518 |
| gross_win_rate | 0.4671 |
| sharpe_ratio | -2.7262 |
| sortino_ratio | -0.6806 |
| max_drawdown | 0.5541 |
| cagr | -0.2671 |
| net_avg_win | 54.6480 |
| net_avg_loss | -81.3457 |
| avg_hold_time_bars | 7.8947 |
| exposure | 0.1091 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
