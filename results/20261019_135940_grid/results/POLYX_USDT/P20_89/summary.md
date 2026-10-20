# EMA Hourly Continuation — POLYX/USDT P20_89

**Symbol:** POLYX/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.6716 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 0.9831 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -3.7940 |
| sortino_ratio | -1.3988 |
| max_drawdown | 0.8308 |
| cagr | -0.4884 |
| net_avg_win | 50.0099 |
| net_avg_loss | -69.6504 |
| avg_hold_time_bars | 12.4136 |
| exposure | 0.3888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
