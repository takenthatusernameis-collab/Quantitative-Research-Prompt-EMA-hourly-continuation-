# EMA Hourly Continuation — PEOPLE/USDT P20_21

**Symbol:** PEOPLE/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 189 |
| net_profit_factor | 0.7183 |
| net_win_rate | 0.5079 |
| gross_profit_factor | 1.0487 |
| gross_win_rate | 0.5079 |
| sharpe_ratio | -1.5184 |
| sortino_ratio | -0.2998 |
| max_drawdown | 0.3706 |
| cagr | -0.1280 |
| net_avg_win | 77.5664 |
| net_avg_loss | -111.4731 |
| avg_hold_time_bars | 4.6296 |
| exposure | 0.0396 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
