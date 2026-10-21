# EMA Hourly Continuation — POPCAT/USDT P12_50

**Symbol:** POPCAT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 546 |
| net_profit_factor | 0.7568 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.9097 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -2.3997 |
| sortino_ratio | -0.8604 |
| max_drawdown | 0.5805 |
| cagr | -0.3280 |
| net_avg_win | 69.2578 |
| net_avg_loss | -82.5842 |
| avg_hold_time_bars | 10.8883 |
| exposure | 0.3141 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
