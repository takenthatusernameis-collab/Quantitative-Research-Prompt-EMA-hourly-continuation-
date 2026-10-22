# EMA Hourly Continuation — UQC/USDT P8_200

**Symbol:** UQC/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 178 |
| net_profit_factor | 0.3939 |
| net_win_rate | 0.3258 |
| gross_profit_factor | 0.4892 |
| gross_win_rate | 0.3258 |
| sharpe_ratio | -3.7808 |
| sortino_ratio | -0.7030 |
| max_drawdown | 0.5644 |
| cagr | -0.2792 |
| net_avg_win | 62.9720 |
| net_avg_loss | -77.2752 |
| avg_hold_time_bars | 99.8202 |
| exposure | 0.8042 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
