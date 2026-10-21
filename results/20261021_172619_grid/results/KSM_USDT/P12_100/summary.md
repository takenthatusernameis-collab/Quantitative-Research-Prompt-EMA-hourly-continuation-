# EMA Hourly Continuation — KSM/USDT P12_100

**Symbol:** KSM/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.6811 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.8553 |
| gross_win_rate | 0.4504 |
| sharpe_ratio | -2.9574 |
| sortino_ratio | -0.9028 |
| max_drawdown | 0.6621 |
| cagr | -0.3402 |
| net_avg_win | 66.2288 |
| net_avg_loss | -79.6954 |
| avg_hold_time_bars | 28.5517 |
| exposure | 0.6022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
