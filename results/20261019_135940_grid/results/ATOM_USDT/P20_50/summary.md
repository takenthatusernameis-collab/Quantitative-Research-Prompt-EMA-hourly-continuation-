# EMA Hourly Continuation — ATOM/USDT P20_50

**Symbol:** ATOM/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 929 |
| net_profit_factor | 0.4235 |
| net_win_rate | 0.4467 |
| gross_profit_factor | 0.8527 |
| gross_win_rate | 0.4650 |
| sharpe_ratio | -7.5673 |
| sortino_ratio | -3.2691 |
| max_drawdown | 0.9821 |
| cagr | -0.7963 |
| net_avg_win | 17.3795 |
| net_avg_loss | -33.1296 |
| avg_hold_time_bars | 4.9300 |
| exposure | 0.2082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
