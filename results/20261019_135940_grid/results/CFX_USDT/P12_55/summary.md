# EMA Hourly Continuation — CFX/USDT P12_55

**Symbol:** CFX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 987 |
| net_profit_factor | 0.5503 |
| net_win_rate | 0.4488 |
| gross_profit_factor | 0.8858 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -6.5206 |
| sortino_ratio | -2.8731 |
| max_drawdown | 0.9707 |
| cagr | -0.7522 |
| net_avg_win | 26.7946 |
| net_avg_loss | -39.6494 |
| avg_hold_time_bars | 8.5623 |
| exposure | 0.3841 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
