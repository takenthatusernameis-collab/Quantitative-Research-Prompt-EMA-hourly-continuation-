# EMA Hourly Continuation — AKT/USDT P34_89

**Symbol:** AKT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.8150 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.0112 |
| gross_win_rate | 0.5063 |
| sharpe_ratio | -1.1985 |
| sortino_ratio | -0.3435 |
| max_drawdown | 0.3420 |
| cagr | -0.1475 |
| net_avg_win | 72.0233 |
| net_avg_loss | -90.6171 |
| avg_hold_time_bars | 10.9148 |
| exposure | 0.1980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
