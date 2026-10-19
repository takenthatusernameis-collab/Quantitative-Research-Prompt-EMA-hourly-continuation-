# EMA Hourly Continuation — BCH/USDT P89_200

**Symbol:** BCH/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.5817 |
| net_win_rate | 0.4895 |
| gross_profit_factor | 1.0010 |
| gross_win_rate | 0.5079 |
| sharpe_ratio | -3.1147 |
| sortino_ratio | -0.8590 |
| max_drawdown | 0.6538 |
| cagr | -0.3370 |
| net_avg_win | 47.8693 |
| net_avg_loss | -78.9187 |
| avg_hold_time_bars | 11.0262 |
| exposure | 0.1915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
