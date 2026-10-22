# EMA Hourly Continuation — RUNE/USDT P21_89

**Symbol:** RUNE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.6249 |
| net_win_rate | 0.4927 |
| gross_profit_factor | 0.9672 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -3.3358 |
| sortino_ratio | -1.1066 |
| max_drawdown | 0.7479 |
| cagr | -0.4095 |
| net_avg_win | 45.0925 |
| net_avg_loss | -70.0954 |
| avg_hold_time_bars | 19.8436 |
| exposure | 0.4961 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
