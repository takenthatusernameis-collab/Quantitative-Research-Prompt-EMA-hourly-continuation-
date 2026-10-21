# EMA Hourly Continuation — NEO/USDT P12_200

**Symbol:** NEO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.7876 |
| net_win_rate | 0.4947 |
| gross_profit_factor | 0.9702 |
| gross_win_rate | 0.4947 |
| sharpe_ratio | -1.1799 |
| sortino_ratio | -0.2826 |
| max_drawdown | 0.3253 |
| cagr | -0.1229 |
| net_avg_win | 74.8229 |
| net_avg_loss | -92.9949 |
| avg_hold_time_bars | 58.2527 |
| exposure | 0.7440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
