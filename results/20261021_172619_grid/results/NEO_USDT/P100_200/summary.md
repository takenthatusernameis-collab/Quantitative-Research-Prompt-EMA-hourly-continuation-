# EMA Hourly Continuation — NEO/USDT P100_200

**Symbol:** NEO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.6217 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.8499 |
| gross_win_rate | 0.4676 |
| sharpe_ratio | -2.3222 |
| sortino_ratio | -0.5529 |
| max_drawdown | 0.4787 |
| cagr | -0.2243 |
| net_avg_win | 59.6120 |
| net_avg_loss | -84.2243 |
| avg_hold_time_bars | 10.6367 |
| exposure | 0.1344 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
