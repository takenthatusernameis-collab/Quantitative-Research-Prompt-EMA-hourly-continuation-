# EMA Hourly Continuation — RSR/USDT P50_89

**Symbol:** RSR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.5780 |
| net_win_rate | 0.4675 |
| gross_profit_factor | 0.9213 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -4.5966 |
| sortino_ratio | -1.6900 |
| max_drawdown | 0.8711 |
| cagr | -0.5532 |
| net_avg_win | 37.6156 |
| net_avg_loss | -57.1228 |
| avg_hold_time_bars | 4.6509 |
| exposure | 0.1429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
