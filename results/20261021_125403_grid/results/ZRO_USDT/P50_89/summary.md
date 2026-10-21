# EMA Hourly Continuation — ZRO/USDT P50_89

**Symbol:** ZRO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.9808 |
| net_win_rate | 0.5528 |
| gross_profit_factor | 1.2242 |
| gross_win_rate | 0.5528 |
| sharpe_ratio | -0.0572 |
| sortino_ratio | -0.0155 |
| max_drawdown | 0.1952 |
| cagr | -0.0135 |
| net_avg_win | 89.4157 |
| net_avg_loss | -112.6959 |
| avg_hold_time_bars | 6.9348 |
| exposure | 0.1093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
