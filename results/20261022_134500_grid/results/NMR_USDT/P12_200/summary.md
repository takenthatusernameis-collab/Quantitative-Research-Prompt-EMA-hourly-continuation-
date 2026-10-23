# EMA Hourly Continuation — NMR/USDT P12_200

**Symbol:** NMR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.6895 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 0.9452 |
| gross_win_rate | 0.4944 |
| sharpe_ratio | -2.2577 |
| sortino_ratio | -0.6743 |
| max_drawdown | 0.5787 |
| cagr | -0.2740 |
| net_avg_win | 56.0363 |
| net_avg_loss | -77.3805 |
| avg_hold_time_bars | 34.9087 |
| exposure | 0.7125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
