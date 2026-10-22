# EMA Hourly Continuation — MEW/USDT P55_100

**Symbol:** MEW/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.6007 |
| net_win_rate | 0.4416 |
| gross_profit_factor | 0.7591 |
| gross_win_rate | 0.4416 |
| sharpe_ratio | -2.8007 |
| sortino_ratio | -0.7443 |
| max_drawdown | 0.5858 |
| cagr | -0.2894 |
| net_avg_win | 55.9004 |
| net_avg_loss | -73.5926 |
| avg_hold_time_bars | 8.8091 |
| exposure | 0.1405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
