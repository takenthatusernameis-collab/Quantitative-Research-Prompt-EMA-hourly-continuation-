# EMA Hourly Continuation — UQC/USDT P12_50

**Symbol:** UQC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.4798 |
| net_win_rate | 0.3623 |
| gross_profit_factor | 0.6607 |
| gross_win_rate | 0.3696 |
| sharpe_ratio | -4.2751 |
| sortino_ratio | -0.9946 |
| max_drawdown | 0.7018 |
| cagr | -0.3722 |
| net_avg_win | 63.7190 |
| net_avg_loss | -75.4581 |
| avg_hold_time_bars | 49.4094 |
| exposure | 0.6172 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
