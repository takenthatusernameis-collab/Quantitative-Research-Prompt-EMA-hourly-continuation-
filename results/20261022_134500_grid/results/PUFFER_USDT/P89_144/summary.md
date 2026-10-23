# EMA Hourly Continuation — PUFFER/USDT P89_144

**Symbol:** PUFFER/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.5111 |
| net_win_rate | 0.4472 |
| gross_profit_factor | 0.7877 |
| gross_win_rate | 0.4500 |
| sharpe_ratio | -4.1233 |
| sortino_ratio | -1.2360 |
| max_drawdown | 0.6961 |
| cagr | -0.4415 |
| net_avg_win | 44.8793 |
| net_avg_loss | -71.0424 |
| avg_hold_time_bars | 6.9972 |
| exposure | 0.1425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
