# EMA Hourly Continuation — BTC/USDT P20_26

**Symbol:** BTC/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 182 |
| net_profit_factor | 0.5118 |
| net_win_rate | 0.5220 |
| gross_profit_factor | 1.0931 |
| gross_win_rate | 0.5275 |
| sharpe_ratio | -2.4370 |
| sortino_ratio | -0.4461 |
| max_drawdown | 0.4476 |
| cagr | -0.1869 |
| net_avg_win | 49.2178 |
| net_avg_loss | -105.0041 |
| avg_hold_time_bars | 5.8571 |
| exposure | 0.0426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
