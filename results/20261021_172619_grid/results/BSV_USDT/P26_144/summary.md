# EMA Hourly Continuation — BSV/USDT P26_144

**Symbol:** BSV/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.6306 |
| net_win_rate | 0.4418 |
| gross_profit_factor | 0.8033 |
| gross_win_rate | 0.4418 |
| sharpe_ratio | -3.0937 |
| sortino_ratio | -0.8984 |
| max_drawdown | 0.6486 |
| cagr | -0.3384 |
| net_avg_win | 59.2634 |
| net_avg_loss | -74.3783 |
| avg_hold_time_bars | 23.4038 |
| exposure | 0.4479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
