# EMA Hourly Continuation — ARKM/USDT P21_34

**Symbol:** ARKM/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1168 |
| net_profit_factor | 0.5130 |
| net_win_rate | 0.4332 |
| gross_profit_factor | 0.9665 |
| gross_win_rate | 0.4572 |
| sharpe_ratio | -9.2664 |
| sortino_ratio | -4.4836 |
| max_drawdown | 0.9963 |
| cagr | -0.8914 |
| net_avg_win | 20.7389 |
| net_avg_loss | -30.9003 |
| avg_hold_time_bars | 2.5437 |
| exposure | 0.1350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
