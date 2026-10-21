# EMA Hourly Continuation — XMR/USDT P55_200

**Symbol:** XMR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.7827 |
| net_win_rate | 0.5032 |
| gross_profit_factor | 1.0244 |
| gross_win_rate | 0.5032 |
| sharpe_ratio | -1.3873 |
| sortino_ratio | -0.3494 |
| max_drawdown | 0.4007 |
| cagr | -0.1481 |
| net_avg_win | 76.9989 |
| net_avg_loss | -99.6675 |
| avg_hold_time_bars | 24.4935 |
| exposure | 0.3429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
