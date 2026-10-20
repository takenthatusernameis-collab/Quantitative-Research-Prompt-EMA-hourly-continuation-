# EMA Hourly Continuation — IOTX/USDT P12_26

**Symbol:** IOTX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1386 |
| net_profit_factor | 0.4773 |
| net_win_rate | 0.4394 |
| gross_profit_factor | 0.9489 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -10.2889 |
| sortino_ratio | -5.4398 |
| max_drawdown | 0.9988 |
| cagr | -0.9312 |
| net_avg_win | 14.9740 |
| net_avg_loss | -24.5909 |
| avg_hold_time_bars | 3.0469 |
| exposure | 0.1920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
