# EMA Hourly Continuation — CAKE/USDT P55_89

**Symbol:** CAKE/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 606 |
| net_profit_factor | 0.3762 |
| net_win_rate | 0.4340 |
| gross_profit_factor | 0.8318 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -6.9174 |
| sortino_ratio | -2.4040 |
| max_drawdown | 0.9578 |
| cagr | -0.7090 |
| net_avg_win | 21.9015 |
| net_avg_loss | -44.6341 |
| avg_hold_time_bars | 4.6881 |
| exposure | 0.1291 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
