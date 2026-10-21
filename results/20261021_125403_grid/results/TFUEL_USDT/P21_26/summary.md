# EMA Hourly Continuation — TFUEL/USDT P21_26

**Symbol:** TFUEL/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.4563 |
| net_win_rate | 0.4007 |
| gross_profit_factor | 0.7130 |
| gross_win_rate | 0.4007 |
| sharpe_ratio | -4.2365 |
| sortino_ratio | -0.9907 |
| max_drawdown | 0.6961 |
| cagr | -0.3689 |
| net_avg_win | 53.8812 |
| net_avg_loss | -78.9615 |
| avg_hold_time_bars | 5.3745 |
| exposure | 0.0649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
