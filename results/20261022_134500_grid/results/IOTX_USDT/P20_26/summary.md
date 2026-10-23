# EMA Hourly Continuation — IOTX/USDT P20_26

**Symbol:** IOTX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1201 |
| net_profit_factor | 0.2513 |
| net_win_rate | 0.3672 |
| gross_profit_factor | 0.7628 |
| gross_win_rate | 0.4147 |
| sharpe_ratio | -14.4402 |
| sortino_ratio | -7.3184 |
| max_drawdown | 0.9999 |
| cagr | -0.9789 |
| net_avg_win | 7.6121 |
| net_avg_loss | -17.5741 |
| avg_hold_time_bars | 2.0391 |
| exposure | 0.1113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
