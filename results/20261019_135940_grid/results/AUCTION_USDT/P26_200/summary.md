# EMA Hourly Continuation — AUCTION/USDT P26_200

**Symbol:** AUCTION/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.5514 |
| net_win_rate | 0.4454 |
| gross_profit_factor | 0.8174 |
| gross_win_rate | 0.4540 |
| sharpe_ratio | -4.0372 |
| sortino_ratio | -1.2092 |
| max_drawdown | 0.7857 |
| cagr | -0.4509 |
| net_avg_win | 46.0669 |
| net_avg_loss | -67.0936 |
| avg_hold_time_bars | 26.3019 |
| exposure | 0.5559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
