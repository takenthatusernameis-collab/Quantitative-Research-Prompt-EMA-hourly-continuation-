# EMA Hourly Continuation — AUCTION/USDT P20_34

**Symbol:** AUCTION/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.4848 |
| net_win_rate | 0.4232 |
| gross_profit_factor | 0.7409 |
| gross_win_rate | 0.4253 |
| sharpe_ratio | -5.3235 |
| sortino_ratio | -1.6626 |
| max_drawdown | 0.8658 |
| cagr | -0.5445 |
| net_avg_win | 39.7729 |
| net_avg_loss | -60.2060 |
| avg_hold_time_bars | 6.4336 |
| exposure | 0.1403 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
