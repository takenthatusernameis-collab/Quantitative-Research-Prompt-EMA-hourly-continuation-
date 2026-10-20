# EMA Hourly Continuation — RPL/USDT P34_200

**Symbol:** RPL/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.8459 |
| net_win_rate | 0.5154 |
| gross_profit_factor | 1.0818 |
| gross_win_rate | 0.5185 |
| sharpe_ratio | -0.9347 |
| sortino_ratio | -0.2393 |
| max_drawdown | 0.3013 |
| cagr | -0.1075 |
| net_avg_win | 81.9862 |
| net_avg_loss | -103.0909 |
| avg_hold_time_bars | 38.5123 |
| exposure | 0.5647 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
