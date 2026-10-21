# EMA Hourly Continuation — TAO/USDT P8_100

**Symbol:** TAO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.9566 |
| net_win_rate | 0.5288 |
| gross_profit_factor | 1.1142 |
| gross_win_rate | 0.5288 |
| sharpe_ratio | -0.2807 |
| sortino_ratio | -0.0892 |
| max_drawdown | 0.3473 |
| cagr | -0.0476 |
| net_avg_win | 98.9042 |
| net_avg_loss | -116.0325 |
| avg_hold_time_bars | 28.4568 |
| exposure | 0.6286 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
