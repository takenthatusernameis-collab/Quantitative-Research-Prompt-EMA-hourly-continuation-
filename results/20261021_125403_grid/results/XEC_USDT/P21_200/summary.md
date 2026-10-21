# EMA Hourly Continuation — XEC/USDT P21_200

**Symbol:** XEC/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.8717 |
| net_win_rate | 0.5262 |
| gross_profit_factor | 1.0984 |
| gross_win_rate | 0.5262 |
| sharpe_ratio | -0.7788 |
| sortino_ratio | -0.2129 |
| max_drawdown | 0.3586 |
| cagr | -0.0959 |
| net_avg_win | 79.9072 |
| net_avg_loss | -101.7932 |
| avg_hold_time_bars | 36.2865 |
| exposure | 0.5960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
