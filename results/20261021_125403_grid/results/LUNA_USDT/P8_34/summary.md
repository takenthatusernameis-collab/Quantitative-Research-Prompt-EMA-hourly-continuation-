# EMA Hourly Continuation — LUNA/USDT P8_34

**Symbol:** LUNA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.7415 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9794 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -3.1173 |
| sortino_ratio | -1.1645 |
| max_drawdown | 0.7471 |
| cagr | -0.4143 |
| net_avg_win | 65.0452 |
| net_avg_loss | -79.8754 |
| avg_hold_time_bars | 7.9810 |
| exposure | 0.2481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
