# EMA Hourly Continuation — COTI/USDT P50_55

**Symbol:** COTI/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 77 |
| net_profit_factor | 0.5933 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8133 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -1.3572 |
| sortino_ratio | -0.1700 |
| max_drawdown | 0.2221 |
| cagr | -0.0750 |
| net_avg_win | 74.0839 |
| net_avg_loss | -104.0509 |
| avg_hold_time_bars | 4.8571 |
| exposure | 0.0170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
