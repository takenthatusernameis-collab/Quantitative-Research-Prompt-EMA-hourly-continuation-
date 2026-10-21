# EMA Hourly Continuation — ZETA/USDT P34_89

**Symbol:** ZETA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.7963 |
| net_win_rate | 0.5022 |
| gross_profit_factor | 1.0283 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -1.6807 |
| sortino_ratio | -0.5134 |
| max_drawdown | 0.4924 |
| cagr | -0.2108 |
| net_avg_win | 76.7678 |
| net_avg_loss | -97.2560 |
| avg_hold_time_bars | 10.9430 |
| exposure | 0.2258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
