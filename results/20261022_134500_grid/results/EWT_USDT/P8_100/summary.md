# EMA Hourly Continuation — EWT/USDT P8_100

**Symbol:** EWT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 809 |
| net_profit_factor | 0.4916 |
| net_win_rate | 0.4265 |
| gross_profit_factor | 0.7390 |
| gross_win_rate | 0.4326 |
| sharpe_ratio | -5.9766 |
| sortino_ratio | -2.3639 |
| max_drawdown | 0.9529 |
| cagr | -0.6864 |
| net_avg_win | 26.5023 |
| net_avg_loss | -40.0859 |
| avg_hold_time_bars | 14.3387 |
| exposure | 0.5273 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
