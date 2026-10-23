# EMA Hourly Continuation — CSPR/USDT P21_55

**Symbol:** CSPR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1241 |
| net_profit_factor | 0.3717 |
| net_win_rate | 0.3916 |
| gross_profit_factor | 0.7525 |
| gross_win_rate | 0.4126 |
| sharpe_ratio | -10.5244 |
| sortino_ratio | -5.2170 |
| max_drawdown | 0.9987 |
| cagr | -0.9281 |
| net_avg_win | 12.1579 |
| net_avg_loss | -21.0533 |
| avg_hold_time_bars | 3.9670 |
| exposure | 0.2238 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
