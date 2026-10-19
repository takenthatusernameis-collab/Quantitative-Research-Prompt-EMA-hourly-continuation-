# EMA Hourly Continuation — PENDLE/USDT P26_144

**Symbol:** PENDLE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.6330 |
| net_win_rate | 0.4735 |
| gross_profit_factor | 0.8990 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -3.0273 |
| sortino_ratio | -0.9659 |
| max_drawdown | 0.6910 |
| cagr | -0.3646 |
| net_avg_win | 48.6606 |
| net_avg_loss | -69.1250 |
| avg_hold_time_bars | 21.7917 |
| exposure | 0.5042 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
