# EMA Hourly Continuation — ENA/USDT P100_200

**Symbol:** ENA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 232 |
| net_profit_factor | 0.8877 |
| net_win_rate | 0.5129 |
| gross_profit_factor | 1.0451 |
| gross_win_rate | 0.5129 |
| sharpe_ratio | -0.5423 |
| sortino_ratio | -0.1187 |
| max_drawdown | 0.2230 |
| cagr | -0.0554 |
| net_avg_win | 88.4803 |
| net_avg_loss | -104.9697 |
| avg_hold_time_bars | 11.0948 |
| exposure | 0.1170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
