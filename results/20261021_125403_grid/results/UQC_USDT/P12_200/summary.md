# EMA Hourly Continuation — UQC/USDT P12_200

**Symbol:** UQC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 161 |
| net_profit_factor | 0.3747 |
| net_win_rate | 0.3043 |
| gross_profit_factor | 0.4523 |
| gross_win_rate | 0.3043 |
| sharpe_ratio | -3.8537 |
| sortino_ratio | -0.6802 |
| max_drawdown | 0.5547 |
| cagr | -0.2726 |
| net_avg_win | 67.5038 |
| net_avg_loss | -78.8080 |
| avg_hold_time_bars | 108.3478 |
| exposure | 0.7895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
