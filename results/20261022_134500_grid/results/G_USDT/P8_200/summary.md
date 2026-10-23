# EMA Hourly Continuation — G/USDT P8_200

**Symbol:** G/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.6276 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.8941 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -2.4224 |
| sortino_ratio | -0.6194 |
| max_drawdown | 0.5625 |
| cagr | -0.2588 |
| net_avg_win | 59.2288 |
| net_avg_loss | -83.3436 |
| avg_hold_time_bars | 53.6759 |
| exposure | 0.8185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
