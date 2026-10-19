# EMA Hourly Continuation — TIA/USDT P21_89

**Symbol:** TIA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.7196 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 1.0096 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -3.0395 |
| sortino_ratio | -1.1159 |
| max_drawdown | 0.7533 |
| cagr | -0.4110 |
| net_avg_win | 57.0263 |
| net_avg_loss | -76.0280 |
| avg_hold_time_bars | 12.5533 |
| exposure | 0.3857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
