# EMA Hourly Continuation — NEO/USDT P89_100

**Symbol:** NEO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 123 |
| net_profit_factor | 0.5809 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 0.9249 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -1.8839 |
| sortino_ratio | -0.3004 |
| max_drawdown | 0.3045 |
| cagr | -0.1293 |
| net_avg_win | 69.0146 |
| net_avg_loss | -109.5197 |
| avg_hold_time_bars | 5.3496 |
| exposure | 0.0299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
