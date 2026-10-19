# EMA Hourly Continuation — GRAM/USDT P34_55

**Symbol:** GRAM/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 945 |
| net_profit_factor | 0.2961 |
| net_win_rate | 0.3979 |
| gross_profit_factor | 0.7855 |
| gross_win_rate | 0.4317 |
| sharpe_ratio | -10.9815 |
| sortino_ratio | -4.8389 |
| max_drawdown | 0.9982 |
| cagr | -0.9193 |
| net_avg_win | 11.1679 |
| net_avg_loss | -24.9229 |
| avg_hold_time_bars | 2.7090 |
| exposure | 0.1164 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
