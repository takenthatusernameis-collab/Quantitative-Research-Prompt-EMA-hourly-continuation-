# EMA Hourly Continuation — BSV/USDT P21_26

**Symbol:** BSV/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 204 |
| net_profit_factor | 0.6084 |
| net_win_rate | 0.4804 |
| gross_profit_factor | 0.9624 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -2.3738 |
| sortino_ratio | -0.4875 |
| max_drawdown | 0.4917 |
| cagr | -0.2002 |
| net_avg_win | 68.0662 |
| net_avg_loss | -103.4403 |
| avg_hold_time_bars | 5.4167 |
| exposure | 0.0502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
