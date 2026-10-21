# EMA Hourly Continuation — ORBS/USDT P12_50

**Symbol:** ORBS/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 700 |
| net_profit_factor | 0.5702 |
| net_win_rate | 0.4257 |
| gross_profit_factor | 0.7966 |
| gross_win_rate | 0.4257 |
| sharpe_ratio | -5.3694 |
| sortino_ratio | -2.0193 |
| max_drawdown | 0.9057 |
| cagr | -0.6064 |
| net_avg_win | 40.2453 |
| net_avg_loss | -52.3173 |
| avg_hold_time_bars | 10.4971 |
| exposure | 0.3340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
