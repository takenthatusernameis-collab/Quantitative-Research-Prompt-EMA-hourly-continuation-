# EMA Hourly Continuation — DBR/USDT P12_21

**Symbol:** DBR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 896 |
| net_profit_factor | 0.3752 |
| net_win_rate | 0.3873 |
| gross_profit_factor | 0.9452 |
| gross_win_rate | 0.4487 |
| sharpe_ratio | -12.0716 |
| sortino_ratio | -5.7953 |
| max_drawdown | 0.9975 |
| cagr | -0.9492 |
| net_avg_win | 17.2599 |
| net_avg_loss | -29.0782 |
| avg_hold_time_bars | 3.7835 |
| exposure | 0.1928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
