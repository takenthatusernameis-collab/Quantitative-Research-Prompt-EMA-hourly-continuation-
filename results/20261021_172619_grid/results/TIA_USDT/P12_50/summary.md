# EMA Hourly Continuation — TIA/USDT P12_50

**Symbol:** TIA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 620 |
| net_profit_factor | 0.8286 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 1.0108 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -1.4192 |
| sortino_ratio | -0.5066 |
| max_drawdown | 0.4940 |
| cagr | -0.2099 |
| net_avg_win | 68.7624 |
| net_avg_loss | -85.1550 |
| avg_hold_time_bars | 10.7065 |
| exposure | 0.3017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
