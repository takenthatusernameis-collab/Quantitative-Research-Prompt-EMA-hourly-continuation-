# EMA Hourly Continuation — RLC/USDT P26_55

**Symbol:** RLC/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.6429 |
| net_win_rate | 0.4762 |
| gross_profit_factor | 0.9060 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -3.2247 |
| sortino_ratio | -1.0353 |
| max_drawdown | 0.7025 |
| cagr | -0.3774 |
| net_avg_win | 52.1931 |
| net_avg_loss | -73.8028 |
| avg_hold_time_bars | 6.4385 |
| exposure | 0.1475 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
