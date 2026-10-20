# EMA Hourly Continuation — WAVES/USDT P26_200

**Symbol:** WAVES/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.5444 |
| net_win_rate | 0.4599 |
| gross_profit_factor | 0.8903 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -4.2404 |
| sortino_ratio | -1.3544 |
| max_drawdown | 0.8243 |
| cagr | -0.4868 |
| net_avg_win | 40.2988 |
| net_avg_loss | -63.0374 |
| avg_hold_time_bars | 22.2233 |
| exposure | 0.5293 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
