# EMA Hourly Continuation — AUCTION/USDT P55_100

**Symbol:** AUCTION/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.4758 |
| net_win_rate | 0.4306 |
| gross_profit_factor | 0.8479 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -6.5706 |
| sortino_ratio | -2.3453 |
| max_drawdown | 0.9489 |
| cagr | -0.6849 |
| net_avg_win | 31.1059 |
| net_avg_loss | -49.4301 |
| avg_hold_time_bars | 5.9236 |
| exposure | 0.1718 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
