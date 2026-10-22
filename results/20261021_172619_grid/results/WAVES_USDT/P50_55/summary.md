# EMA Hourly Continuation — WAVES/USDT P50_55

**Symbol:** WAVES/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 140 |
| net_profit_factor | 0.4304 |
| net_win_rate | 0.4071 |
| gross_profit_factor | 0.6884 |
| gross_win_rate | 0.4071 |
| sharpe_ratio | -3.0599 |
| sortino_ratio | -0.5199 |
| max_drawdown | 0.4633 |
| cagr | -0.2169 |
| net_avg_win | 60.8105 |
| net_avg_loss | -97.0359 |
| avg_hold_time_bars | 5.7857 |
| exposure | 0.0368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
