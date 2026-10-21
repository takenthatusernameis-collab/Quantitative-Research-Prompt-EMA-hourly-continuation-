# EMA Hourly Continuation — ADA/USDT P144_200

**Symbol:** ADA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 164 |
| net_profit_factor | 0.7748 |
| net_win_rate | 0.5244 |
| gross_profit_factor | 1.0970 |
| gross_win_rate | 0.5244 |
| sharpe_ratio | -0.9927 |
| sortino_ratio | -0.1837 |
| max_drawdown | 0.2036 |
| cagr | -0.0807 |
| net_avg_win | 76.1855 |
| net_avg_loss | -108.4103 |
| avg_hold_time_bars | 6.9756 |
| exposure | 0.0520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
