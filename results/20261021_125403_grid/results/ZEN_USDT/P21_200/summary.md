# EMA Hourly Continuation — ZEN/USDT P21_200

**Symbol:** ZEN/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.8284 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 0.9899 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -0.9445 |
| sortino_ratio | -0.2186 |
| max_drawdown | 0.2976 |
| cagr | -0.0979 |
| net_avg_win | 84.0622 |
| net_avg_loss | -100.7031 |
| avg_hold_time_bars | 56.5779 |
| exposure | 0.6764 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
