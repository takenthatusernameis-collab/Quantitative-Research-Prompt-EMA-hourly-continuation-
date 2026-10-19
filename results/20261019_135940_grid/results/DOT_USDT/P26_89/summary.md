# EMA Hourly Continuation — DOT/USDT P26_89

**Symbol:** DOT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.6241 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 1.0272 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -4.0596 |
| sortino_ratio | -1.4638 |
| max_drawdown | 0.8354 |
| cagr | -0.5057 |
| net_avg_win | 43.0443 |
| net_avg_loss | -65.6833 |
| avg_hold_time_bars | 10.9619 |
| exposure | 0.3269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
