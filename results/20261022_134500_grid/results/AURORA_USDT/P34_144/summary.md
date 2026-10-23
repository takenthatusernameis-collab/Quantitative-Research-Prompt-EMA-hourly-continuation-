# EMA Hourly Continuation — AURORA/USDT P34_144

**Symbol:** AURORA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.5724 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.8939 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -4.1434 |
| sortino_ratio | -1.2309 |
| max_drawdown | 0.7841 |
| cagr | -0.4512 |
| net_avg_win | 51.5864 |
| net_avg_loss | -74.0002 |
| avg_hold_time_bars | 18.6228 |
| exposure | 0.3792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
