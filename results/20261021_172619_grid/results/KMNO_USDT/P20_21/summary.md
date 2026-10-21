# EMA Hourly Continuation — KMNO/USDT P20_21

**Symbol:** KMNO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 150 |
| net_profit_factor | 0.7137 |
| net_win_rate | 0.5133 |
| gross_profit_factor | 1.0479 |
| gross_win_rate | 0.5133 |
| sharpe_ratio | -1.2916 |
| sortino_ratio | -0.2288 |
| max_drawdown | 0.2722 |
| cagr | -0.1000 |
| net_avg_win | 74.2389 |
| net_avg_loss | -109.7271 |
| avg_hold_time_bars | 5.0000 |
| exposure | 0.0346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
