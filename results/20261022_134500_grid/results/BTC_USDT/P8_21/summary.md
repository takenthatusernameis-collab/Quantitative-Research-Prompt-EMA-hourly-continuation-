# EMA Hourly Continuation — BTC/USDT P8_21

**Symbol:** BTC/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1864 |
| net_profit_factor | 0.1298 |
| net_win_rate | 0.3310 |
| gross_profit_factor | 0.7897 |
| gross_win_rate | 0.4496 |
| sharpe_ratio | -19.3261 |
| sortino_ratio | -11.6990 |
| max_drawdown | 1.0000 |
| cagr | -0.9984 |
| net_avg_win | 2.4166 |
| net_avg_loss | -9.2149 |
| avg_hold_time_bars | 3.2006 |
| exposure | 0.2386 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
