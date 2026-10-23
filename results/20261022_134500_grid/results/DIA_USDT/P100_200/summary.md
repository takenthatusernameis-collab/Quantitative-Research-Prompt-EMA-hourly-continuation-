# EMA Hourly Continuation — DIA/USDT P100_200

**Symbol:** DIA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.7967 |
| net_win_rate | 0.5373 |
| gross_profit_factor | 1.2191 |
| gross_win_rate | 0.5476 |
| sharpe_ratio | -1.4611 |
| sortino_ratio | -0.4110 |
| max_drawdown | 0.4932 |
| cagr | -0.1758 |
| net_avg_win | 72.3694 |
| net_avg_loss | -105.4771 |
| avg_hold_time_bars | 9.8509 |
| exposure | 0.1734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
