# EMA Hourly Continuation — MOG/USDT P34_200

**Symbol:** MOG/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 0.7632 |
| net_win_rate | 0.4729 |
| gross_profit_factor | 0.8817 |
| gross_win_rate | 0.4729 |
| sharpe_ratio | -1.4025 |
| sortino_ratio | -0.3342 |
| max_drawdown | 0.3249 |
| cagr | -0.1431 |
| net_avg_win | 78.8874 |
| net_avg_loss | -92.7189 |
| avg_hold_time_bars | 37.9147 |
| exposure | 0.4863 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
