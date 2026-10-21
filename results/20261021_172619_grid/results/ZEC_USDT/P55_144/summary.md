# EMA Hourly Continuation — ZEC/USDT P55_144

**Symbol:** ZEC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.7973 |
| net_win_rate | 0.4955 |
| gross_profit_factor | 0.9786 |
| gross_win_rate | 0.4955 |
| sharpe_ratio | -1.2214 |
| sortino_ratio | -0.3188 |
| max_drawdown | 0.3671 |
| cagr | -0.1370 |
| net_avg_win | 73.7490 |
| net_avg_loss | -90.8469 |
| avg_hold_time_bars | 14.8258 |
| exposure | 0.2244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
