# EMA Hourly Continuation — AVAX/USDT P34_89

**Symbol:** AVAX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.7561 |
| net_win_rate | 0.4939 |
| gross_profit_factor | 0.9961 |
| gross_win_rate | 0.4939 |
| sharpe_ratio | -1.9735 |
| sortino_ratio | -0.5698 |
| max_drawdown | 0.5206 |
| cagr | -0.2301 |
| net_avg_win | 74.2390 |
| net_avg_loss | -95.8073 |
| avg_hold_time_bars | 10.4521 |
| exposure | 0.1934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
