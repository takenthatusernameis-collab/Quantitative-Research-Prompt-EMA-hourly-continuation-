# EMA Hourly Continuation — RPL/USDT P21_200

**Symbol:** RPL/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.9376 |
| net_win_rate | 0.5244 |
| gross_profit_factor | 1.1004 |
| gross_win_rate | 0.5244 |
| sharpe_ratio | -0.3049 |
| sortino_ratio | -0.0768 |
| max_drawdown | 0.1912 |
| cagr | -0.0389 |
| net_avg_win | 88.8339 |
| net_avg_loss | -104.4849 |
| avg_hold_time_bars | 47.0391 |
| exposure | 0.6535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
