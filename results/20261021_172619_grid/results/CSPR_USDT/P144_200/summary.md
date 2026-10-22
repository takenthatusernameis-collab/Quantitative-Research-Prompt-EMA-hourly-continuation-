# EMA Hourly Continuation — CSPR/USDT P144_200

**Symbol:** CSPR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 194 |
| net_profit_factor | 0.6290 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.8299 |
| gross_win_rate | 0.4588 |
| sharpe_ratio | -1.9172 |
| sortino_ratio | -0.3806 |
| max_drawdown | 0.3637 |
| cagr | -0.1605 |
| net_avg_win | 67.7425 |
| net_avg_loss | -91.2903 |
| avg_hold_time_bars | 8.0103 |
| exposure | 0.0706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
