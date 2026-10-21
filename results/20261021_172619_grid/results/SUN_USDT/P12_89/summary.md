# EMA Hourly Continuation — SUN/USDT P12_89

**Symbol:** SUN/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.6040 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.9748 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -4.5951 |
| sortino_ratio | -1.4549 |
| max_drawdown | 0.8403 |
| cagr | -0.5005 |
| net_avg_win | 54.5768 |
| net_avg_loss | -76.4513 |
| avg_hold_time_bars | 22.8750 |
| exposure | 0.5217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
