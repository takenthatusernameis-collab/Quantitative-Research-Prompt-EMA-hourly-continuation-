# EMA Hourly Continuation — BOME/USDT P21_34

**Symbol:** BOME/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.6351 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.8251 |
| gross_win_rate | 0.4576 |
| sharpe_ratio | -2.3566 |
| sortino_ratio | -0.5765 |
| max_drawdown | 0.5256 |
| cagr | -0.2327 |
| net_avg_win | 62.6568 |
| net_avg_loss | -83.2352 |
| avg_hold_time_bars | 5.0508 |
| exposure | 0.0677 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
