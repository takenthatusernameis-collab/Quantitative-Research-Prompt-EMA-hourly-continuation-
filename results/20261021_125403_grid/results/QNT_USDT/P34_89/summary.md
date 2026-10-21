# EMA Hourly Continuation — QNT/USDT P34_89

**Symbol:** QNT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.6660 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9286 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -2.6703 |
| sortino_ratio | -0.8478 |
| max_drawdown | 0.6376 |
| cagr | -0.3205 |
| net_avg_win | 51.8023 |
| net_avg_loss | -73.7734 |
| avg_hold_time_bars | 8.4033 |
| exposure | 0.1875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
