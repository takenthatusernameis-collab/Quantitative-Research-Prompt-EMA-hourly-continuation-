# EMA Hourly Continuation — EDU/USDT P8_50

**Symbol:** EDU/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 760 |
| net_profit_factor | 0.7531 |
| net_win_rate | 0.4895 |
| gross_profit_factor | 0.9437 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -2.3171 |
| sortino_ratio | -0.9105 |
| max_drawdown | 0.6567 |
| cagr | -0.3429 |
| net_avg_win | 53.5813 |
| net_avg_loss | -68.2105 |
| avg_hold_time_bars | 13.0987 |
| exposure | 0.4505 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
