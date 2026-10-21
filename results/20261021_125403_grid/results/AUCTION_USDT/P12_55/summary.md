# EMA Hourly Continuation — AUCTION/USDT P12_55

**Symbol:** AUCTION/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.6363 |
| net_win_rate | 0.4529 |
| gross_profit_factor | 0.8582 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -4.2423 |
| sortino_ratio | -1.5501 |
| max_drawdown | 0.8432 |
| cagr | -0.5150 |
| net_avg_win | 48.4224 |
| net_avg_loss | -63.0043 |
| avg_hold_time_bars | 12.6248 |
| exposure | 0.3823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
