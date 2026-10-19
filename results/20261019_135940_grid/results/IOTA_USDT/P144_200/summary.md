# EMA Hourly Continuation — IOTA/USDT P144_200

**Symbol:** IOTA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.4532 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.8488 |
| gross_win_rate | 0.4579 |
| sharpe_ratio | -4.6825 |
| sortino_ratio | -1.2866 |
| max_drawdown | 0.8058 |
| cagr | -0.4733 |
| net_avg_win | 38.7883 |
| net_avg_loss | -70.0203 |
| avg_hold_time_bars | 4.1079 |
| exposure | 0.0710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
