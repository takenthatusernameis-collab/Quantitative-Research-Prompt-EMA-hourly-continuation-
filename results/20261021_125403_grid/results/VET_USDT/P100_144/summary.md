# EMA Hourly Continuation — VET/USDT P100_144

**Symbol:** VET/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.8919 |
| net_win_rate | 0.5595 |
| gross_profit_factor | 1.2578 |
| gross_win_rate | 0.5595 |
| sharpe_ratio | -0.5003 |
| sortino_ratio | -0.1096 |
| max_drawdown | 0.2070 |
| cagr | -0.0511 |
| net_avg_win | 80.2304 |
| net_avg_loss | -114.2442 |
| avg_hold_time_bars | 6.8370 |
| exposure | 0.0705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
