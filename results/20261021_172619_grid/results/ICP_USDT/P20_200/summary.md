# EMA Hourly Continuation — ICP/USDT P20_200

**Symbol:** ICP/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.8236 |
| net_win_rate | 0.4947 |
| gross_profit_factor | 0.9689 |
| gross_win_rate | 0.4947 |
| sharpe_ratio | -0.9985 |
| sortino_ratio | -0.2406 |
| max_drawdown | 0.2865 |
| cagr | -0.1063 |
| net_avg_win | 81.4796 |
| net_avg_loss | -96.8647 |
| avg_hold_time_bars | 49.0491 |
| exposure | 0.6354 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
