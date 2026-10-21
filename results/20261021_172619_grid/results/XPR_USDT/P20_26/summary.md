# EMA Hourly Continuation — XPR/USDT P20_26

**Symbol:** XPR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 108 |
| net_profit_factor | 0.8643 |
| net_win_rate | 0.5556 |
| gross_profit_factor | 1.2352 |
| gross_win_rate | 0.5556 |
| sharpe_ratio | -0.4353 |
| sortino_ratio | -0.0657 |
| max_drawdown | 0.1414 |
| cagr | -0.0303 |
| net_avg_win | 78.9821 |
| net_avg_loss | -114.2334 |
| avg_hold_time_bars | 13.7685 |
| exposure | 0.0676 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
