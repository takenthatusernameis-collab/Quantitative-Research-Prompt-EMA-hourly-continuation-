# EMA Hourly Continuation — TURBO/USDT P21_89

**Symbol:** TURBO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 640 |
| net_profit_factor | 0.6456 |
| net_win_rate | 0.4703 |
| gross_profit_factor | 0.9268 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -4.3142 |
| sortino_ratio | -1.6791 |
| max_drawdown | 0.8220 |
| cagr | -0.5506 |
| net_avg_win | 49.1757 |
| net_avg_loss | -67.6280 |
| avg_hold_time_bars | 10.3609 |
| exposure | 0.3617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
