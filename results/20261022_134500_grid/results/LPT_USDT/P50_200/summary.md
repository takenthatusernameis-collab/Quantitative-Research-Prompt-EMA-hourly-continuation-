# EMA Hourly Continuation — LPT/USDT P50_200

**Symbol:** LPT/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.6474 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.9222 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -2.8759 |
| sortino_ratio | -0.8460 |
| max_drawdown | 0.6498 |
| cagr | -0.3315 |
| net_avg_win | 55.6229 |
| net_avg_loss | -78.7930 |
| avg_hold_time_bars | 18.4123 |
| exposure | 0.3674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
