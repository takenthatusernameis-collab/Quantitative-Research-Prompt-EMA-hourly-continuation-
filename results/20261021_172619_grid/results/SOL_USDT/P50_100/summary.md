# EMA Hourly Continuation — SOL/USDT P50_100

**Symbol:** SOL/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.6857 |
| net_win_rate | 0.4824 |
| gross_profit_factor | 0.9475 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -2.2221 |
| sortino_ratio | -0.5628 |
| max_drawdown | 0.4942 |
| cagr | -0.2282 |
| net_avg_win | 69.0967 |
| net_avg_loss | -93.9200 |
| avg_hold_time_bars | 8.5591 |
| exposure | 0.1218 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
