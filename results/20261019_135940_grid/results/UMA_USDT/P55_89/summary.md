# EMA Hourly Continuation — UMA/USDT P55_89

**Symbol:** UMA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.4940 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.9233 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -5.5172 |
| sortino_ratio | -2.0084 |
| max_drawdown | 0.9136 |
| cagr | -0.6187 |
| net_avg_win | 29.1687 |
| net_avg_loss | -51.3056 |
| avg_hold_time_bars | 5.0915 |
| exposure | 0.1518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
