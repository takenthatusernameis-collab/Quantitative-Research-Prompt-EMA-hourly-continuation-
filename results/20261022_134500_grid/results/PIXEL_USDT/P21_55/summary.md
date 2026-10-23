# EMA Hourly Continuation — PIXEL/USDT P21_55

**Symbol:** PIXEL/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 921 |
| net_profit_factor | 0.5721 |
| net_win_rate | 0.4636 |
| gross_profit_factor | 0.9105 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -5.3866 |
| sortino_ratio | -2.3136 |
| max_drawdown | 0.9407 |
| cagr | -0.6661 |
| net_avg_win | 29.3455 |
| net_avg_loss | -44.3358 |
| avg_hold_time_bars | 6.1010 |
| exposure | 0.2543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
