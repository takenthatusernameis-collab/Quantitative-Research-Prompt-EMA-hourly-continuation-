# EMA Hourly Continuation — ADA/USDT P34_144

**Symbol:** ADA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.8668 |
| net_win_rate | 0.5262 |
| gross_profit_factor | 1.0901 |
| gross_win_rate | 0.5262 |
| sharpe_ratio | -0.7520 |
| sortino_ratio | -0.2008 |
| max_drawdown | 0.2968 |
| cagr | -0.0906 |
| net_avg_win | 76.2528 |
| net_avg_loss | -97.6869 |
| avg_hold_time_bars | 21.7965 |
| exposure | 0.3408 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
