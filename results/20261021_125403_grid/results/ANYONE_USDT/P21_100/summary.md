# EMA Hourly Continuation — ANYONE/USDT P21_100

**Symbol:** ANYONE/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.7254 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.8337 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -2.1236 |
| sortino_ratio | -0.6617 |
| max_drawdown | 0.5154 |
| cagr | -0.2637 |
| net_avg_win | 65.9353 |
| net_avg_loss | -77.3591 |
| avg_hold_time_bars | 16.7862 |
| exposure | 0.3690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
