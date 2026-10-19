# EMA Hourly Continuation — MANA/USDT P21_89

**Symbol:** MANA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.5961 |
| net_win_rate | 0.4423 |
| gross_profit_factor | 0.9569 |
| gross_win_rate | 0.4534 |
| sharpe_ratio | -5.8985 |
| sortino_ratio | -2.2111 |
| max_drawdown | 0.9404 |
| cagr | -0.6660 |
| net_avg_win | 43.4617 |
| net_avg_loss | -57.8151 |
| avg_hold_time_bars | 11.3602 |
| exposure | 0.3713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
