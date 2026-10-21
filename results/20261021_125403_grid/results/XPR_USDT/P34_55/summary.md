# EMA Hourly Continuation — XPR/USDT P34_55

**Symbol:** XPR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 165 |
| net_profit_factor | 0.7852 |
| net_win_rate | 0.5212 |
| gross_profit_factor | 1.0796 |
| gross_win_rate | 0.5212 |
| sharpe_ratio | -0.9444 |
| sortino_ratio | -0.1749 |
| max_drawdown | 0.2250 |
| cagr | -0.0773 |
| net_avg_win | 77.7861 |
| net_avg_loss | -107.8474 |
| avg_hold_time_bars | 13.6424 |
| exposure | 0.1023 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
