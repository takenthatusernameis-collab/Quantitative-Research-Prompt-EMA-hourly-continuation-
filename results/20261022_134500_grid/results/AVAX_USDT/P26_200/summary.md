# EMA Hourly Continuation — AVAX/USDT P26_200

**Symbol:** AVAX/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.7953 |
| net_win_rate | 0.5325 |
| gross_profit_factor | 1.1820 |
| gross_win_rate | 0.5422 |
| sharpe_ratio | -1.2542 |
| sortino_ratio | -0.3126 |
| max_drawdown | 0.4016 |
| cagr | -0.1374 |
| net_avg_win | 73.4696 |
| net_avg_loss | -105.2119 |
| avg_hold_time_bars | 41.6169 |
| exposure | 0.5826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
