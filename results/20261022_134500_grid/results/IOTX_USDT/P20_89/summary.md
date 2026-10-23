# EMA Hourly Continuation — IOTX/USDT P20_89

**Symbol:** IOTX/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 773 |
| net_profit_factor | 0.5758 |
| net_win_rate | 0.4605 |
| gross_profit_factor | 0.8913 |
| gross_win_rate | 0.4709 |
| sharpe_ratio | -5.1197 |
| sortino_ratio | -2.0031 |
| max_drawdown | 0.9128 |
| cagr | -0.6173 |
| net_avg_win | 34.7167 |
| net_avg_loss | -51.4701 |
| avg_hold_time_bars | 10.1514 |
| exposure | 0.3567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
