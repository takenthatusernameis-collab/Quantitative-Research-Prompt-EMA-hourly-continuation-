# EMA Hourly Continuation — MOCA/USDT P21_144

**Symbol:** MOCA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.6109 |
| net_win_rate | 0.4594 |
| gross_profit_factor | 0.9154 |
| gross_win_rate | 0.4710 |
| sharpe_ratio | -3.6975 |
| sortino_ratio | -1.1262 |
| max_drawdown | 0.7267 |
| cagr | -0.4225 |
| net_avg_win | 56.5727 |
| net_avg_loss | -78.6975 |
| avg_hold_time_bars | 24.9629 |
| exposure | 0.5394 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
