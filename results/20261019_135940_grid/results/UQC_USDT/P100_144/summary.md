# EMA Hourly Continuation — UQC/USDT P100_144

**Symbol:** UQC/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.1119 |
| net_win_rate | 0.2096 |
| gross_profit_factor | 0.3310 |
| gross_win_rate | 0.2550 |
| sharpe_ratio | -10.2286 |
| sortino_ratio | -2.9093 |
| max_drawdown | 0.9846 |
| cagr | -0.8088 |
| net_avg_win | 16.7676 |
| net_avg_loss | -39.7374 |
| avg_hold_time_bars | 17.9830 |
| exposure | 0.2873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
