# EMA Hourly Continuation — W/USDT P21_200

**Symbol:** W/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.9549 |
| net_win_rate | 0.5260 |
| gross_profit_factor | 1.0962 |
| gross_win_rate | 0.5260 |
| sharpe_ratio | -0.2090 |
| sortino_ratio | -0.0528 |
| max_drawdown | 0.2323 |
| cagr | -0.0289 |
| net_avg_win | 92.7641 |
| net_avg_loss | -107.7962 |
| avg_hold_time_bars | 45.3312 |
| exposure | 0.6346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
