# EMA Hourly Continuation — BIGTIME/USDT P34_50

**Symbol:** BIGTIME/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.7553 |
| net_win_rate | 0.5291 |
| gross_profit_factor | 1.0982 |
| gross_win_rate | 0.5291 |
| sharpe_ratio | -1.5131 |
| sortino_ratio | -0.3943 |
| max_drawdown | 0.3872 |
| cagr | -0.1646 |
| net_avg_win | 65.0638 |
| net_avg_loss | -96.7730 |
| avg_hold_time_bars | 6.1651 |
| exposure | 0.0912 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
