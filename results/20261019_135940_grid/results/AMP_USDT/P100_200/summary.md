# EMA Hourly Continuation — AMP/USDT P100_200

**Symbol:** AMP/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.3631 |
| net_win_rate | 0.3980 |
| gross_profit_factor | 0.6338 |
| gross_win_rate | 0.4099 |
| sharpe_ratio | -6.1057 |
| sortino_ratio | -1.9429 |
| max_drawdown | 0.9068 |
| cagr | -0.6098 |
| net_avg_win | 25.6916 |
| net_avg_loss | -46.7859 |
| avg_hold_time_bars | 9.4416 |
| exposure | 0.2167 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
