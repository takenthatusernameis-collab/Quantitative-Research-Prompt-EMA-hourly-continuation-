# EMA Hourly Continuation — BAND/USDT P26_34

**Symbol:** BAND/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 994 |
| net_profit_factor | 0.3224 |
| net_win_rate | 0.4095 |
| gross_profit_factor | 0.9273 |
| gross_win_rate | 0.4588 |
| sharpe_ratio | -10.8100 |
| sortino_ratio | -4.8818 |
| max_drawdown | 0.9982 |
| cagr | -0.9168 |
| net_avg_win | 11.6707 |
| net_avg_loss | -25.0956 |
| avg_hold_time_bars | 2.8491 |
| exposure | 0.1282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
