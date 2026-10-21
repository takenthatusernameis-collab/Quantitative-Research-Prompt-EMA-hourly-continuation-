# EMA Hourly Continuation — TRB/USDT P21_200

**Symbol:** TRB/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.7348 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.8739 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -1.5645 |
| sortino_ratio | -0.3588 |
| max_drawdown | 0.3537 |
| cagr | -0.1523 |
| net_avg_win | 77.4153 |
| net_avg_loss | -91.8049 |
| avg_hold_time_bars | 56.4160 |
| exposure | 0.6689 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
