# EMA Hourly Continuation — AKT/USDT P26_89

**Symbol:** AKT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.8611 |
| net_win_rate | 0.5146 |
| gross_profit_factor | 1.0535 |
| gross_win_rate | 0.5146 |
| sharpe_ratio | -0.9533 |
| sortino_ratio | -0.2890 |
| max_drawdown | 0.3022 |
| cagr | -0.1274 |
| net_avg_win | 78.4160 |
| net_avg_loss | -96.5484 |
| avg_hold_time_bars | 13.3461 |
| exposure | 0.2700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
