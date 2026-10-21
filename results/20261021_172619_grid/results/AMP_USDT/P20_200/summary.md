# EMA Hourly Continuation — AMP/USDT P20_200

**Symbol:** AMP/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.5932 |
| net_win_rate | 0.4332 |
| gross_profit_factor | 0.7426 |
| gross_win_rate | 0.4332 |
| sharpe_ratio | -3.2101 |
| sortino_ratio | -0.9455 |
| max_drawdown | 0.6807 |
| cagr | -0.3546 |
| net_avg_win | 51.7407 |
| net_avg_loss | -66.6545 |
| avg_hold_time_bars | 29.7972 |
| exposure | 0.5878 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
