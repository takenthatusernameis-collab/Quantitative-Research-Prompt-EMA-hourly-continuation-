# EMA Hourly Continuation — RUNE/USDT P8_26

**Symbol:** RUNE/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1530 |
| net_profit_factor | 0.4787 |
| net_win_rate | 0.4359 |
| gross_profit_factor | 0.9394 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -10.8860 |
| sortino_ratio | -6.0030 |
| max_drawdown | 0.9995 |
| cagr | -0.9511 |
| net_avg_win | 13.7584 |
| net_avg_loss | -22.2152 |
| avg_hold_time_bars | 3.5719 |
| exposure | 0.2484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
