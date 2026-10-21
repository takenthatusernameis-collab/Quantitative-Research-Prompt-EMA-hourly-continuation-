# EMA Hourly Continuation — WAVES/USDT P21_89

**Symbol:** WAVES/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 554 |
| net_profit_factor | 0.7106 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 0.9567 |
| gross_win_rate | 0.4838 |
| sharpe_ratio | -2.7591 |
| sortino_ratio | -0.9275 |
| max_drawdown | 0.7075 |
| cagr | -0.3481 |
| net_avg_win | 60.3467 |
| net_avg_loss | -79.5750 |
| avg_hold_time_bars | 14.1047 |
| exposure | 0.3552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
