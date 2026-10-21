# EMA Hourly Continuation — FLR/USDT P21_144

**Symbol:** FLR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.6773 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.8683 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -2.6493 |
| sortino_ratio | -0.8090 |
| max_drawdown | 0.6124 |
| cagr | -0.3109 |
| net_avg_win | 59.5816 |
| net_avg_loss | -76.2138 |
| avg_hold_time_bars | 21.9154 |
| exposure | 0.4592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
