# EMA Hourly Continuation — UMA/USDT P26_34

**Symbol:** UMA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1049 |
| net_profit_factor | 0.2828 |
| net_win_rate | 0.3880 |
| gross_profit_factor | 0.7970 |
| gross_win_rate | 0.4376 |
| sharpe_ratio | -11.8291 |
| sortino_ratio | -5.5084 |
| max_drawdown | 0.9992 |
| cagr | -0.9407 |
| net_avg_win | 9.6807 |
| net_avg_loss | -21.7005 |
| avg_hold_time_bars | 2.7788 |
| exposure | 0.1325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
