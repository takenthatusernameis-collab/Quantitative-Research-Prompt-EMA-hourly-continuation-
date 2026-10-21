# EMA Hourly Continuation — RENDER/USDT P8_50

**Symbol:** RENDER/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.8380 |
| net_win_rate | 0.5151 |
| gross_profit_factor | 1.0374 |
| gross_win_rate | 0.5151 |
| sharpe_ratio | -1.3553 |
| sortino_ratio | -0.5259 |
| max_drawdown | 0.4949 |
| cagr | -0.2187 |
| net_avg_win | 66.0294 |
| net_avg_loss | -83.7019 |
| avg_hold_time_bars | 11.8919 |
| exposure | 0.3948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
