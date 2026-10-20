# EMA Hourly Continuation — WEMIX/USDT P100_200

**Symbol:** WEMIX/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.3303 |
| net_win_rate | 0.3211 |
| gross_profit_factor | 0.5338 |
| gross_win_rate | 0.3291 |
| sharpe_ratio | -9.1793 |
| sortino_ratio | -3.2680 |
| max_drawdown | 0.9826 |
| cagr | -0.8003 |
| net_avg_win | 24.1088 |
| net_avg_loss | -34.5195 |
| avg_hold_time_bars | 7.3466 |
| exposure | 0.2090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
