# EMA Hourly Continuation — LSK/USDT P89_144

**Symbol:** LSK/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.5193 |
| net_win_rate | 0.4610 |
| gross_profit_factor | 0.9171 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -4.1413 |
| sortino_ratio | -1.2211 |
| max_drawdown | 0.7871 |
| cagr | -0.4447 |
| net_avg_win | 41.4720 |
| net_avg_loss | -68.3122 |
| avg_hold_time_bars | 7.6514 |
| exposure | 0.1516 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
