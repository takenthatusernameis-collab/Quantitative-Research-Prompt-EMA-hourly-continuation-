# EMA Hourly Continuation — PEPE/USDT P8_89

**Symbol:** PEPE/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.6314 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.9374 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -3.9395 |
| sortino_ratio | -1.4385 |
| max_drawdown | 0.8373 |
| cagr | -0.5083 |
| net_avg_win | 43.4443 |
| net_avg_loss | -62.6892 |
| avg_hold_time_bars | 20.4302 |
| exposure | 0.6389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
