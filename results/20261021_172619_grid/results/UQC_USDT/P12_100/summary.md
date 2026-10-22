# EMA Hourly Continuation — UQC/USDT P12_100

**Symbol:** UQC/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 220 |
| net_profit_factor | 0.3602 |
| net_win_rate | 0.2955 |
| gross_profit_factor | 0.5223 |
| gross_win_rate | 0.3182 |
| sharpe_ratio | -5.4789 |
| sortino_ratio | -1.1271 |
| max_drawdown | 0.7772 |
| cagr | -0.4456 |
| net_avg_win | 67.0537 |
| net_avg_loss | -78.0615 |
| avg_hold_time_bars | 68.9000 |
| exposure | 0.6860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
