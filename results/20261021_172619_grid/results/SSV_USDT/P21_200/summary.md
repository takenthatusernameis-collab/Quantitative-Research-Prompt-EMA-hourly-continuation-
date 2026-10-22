# EMA Hourly Continuation — SSV/USDT P21_200

**Symbol:** SSV/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.8206 |
| net_win_rate | 0.4927 |
| gross_profit_factor | 0.9685 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -0.9831 |
| sortino_ratio | -0.2317 |
| max_drawdown | 0.2940 |
| cagr | -0.1025 |
| net_avg_win | 80.9085 |
| net_avg_loss | -95.7547 |
| avg_hold_time_bars | 52.7774 |
| exposure | 0.6544 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
