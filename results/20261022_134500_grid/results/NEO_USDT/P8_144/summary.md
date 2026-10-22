# EMA Hourly Continuation — NEO/USDT P8_144

**Symbol:** NEO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.6529 |
| net_win_rate | 0.4951 |
| gross_profit_factor | 0.9875 |
| gross_win_rate | 0.5073 |
| sharpe_ratio | -2.3897 |
| sortino_ratio | -0.6858 |
| max_drawdown | 0.6202 |
| cagr | -0.2765 |
| net_avg_win | 51.3102 |
| net_avg_loss | -77.0751 |
| avg_hold_time_bars | 42.1699 |
| exposure | 0.7897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
