# EMA Hourly Continuation — AZERO/USDT P20_34

**Symbol:** AZERO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 989 |
| net_profit_factor | 0.3937 |
| net_win_rate | 0.4226 |
| gross_profit_factor | 0.9172 |
| gross_win_rate | 0.4368 |
| sharpe_ratio | -8.9442 |
| sortino_ratio | -3.9532 |
| max_drawdown | 0.9936 |
| cagr | -0.8638 |
| net_avg_win | 15.4312 |
| net_avg_loss | -28.6948 |
| avg_hold_time_bars | 3.8119 |
| exposure | 0.1706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
