# EMA Hourly Continuation — API3/USDT P34_200

**Symbol:** API3/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.8593 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0206 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -0.8684 |
| sortino_ratio | -0.2236 |
| max_drawdown | 0.3918 |
| cagr | -0.0997 |
| net_avg_win | 86.8892 |
| net_avg_loss | -103.0099 |
| avg_hold_time_bars | 34.6625 |
| exposure | 0.5089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
