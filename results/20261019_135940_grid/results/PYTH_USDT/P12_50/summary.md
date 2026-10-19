# EMA Hourly Continuation — PYTH/USDT P12_50

**Symbol:** PYTH/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1047 |
| net_profit_factor | 0.5955 |
| net_win_rate | 0.4747 |
| gross_profit_factor | 0.9128 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -5.4482 |
| sortino_ratio | -2.4739 |
| max_drawdown | 0.9522 |
| cagr | -0.6981 |
| net_avg_win | 28.1611 |
| net_avg_loss | -42.7305 |
| avg_hold_time_bars | 7.1585 |
| exposure | 0.3407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
