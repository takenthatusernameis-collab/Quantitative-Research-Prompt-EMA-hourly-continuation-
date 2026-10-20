# EMA Hourly Continuation — AUCTION/USDT P8_100

**Symbol:** AUCTION/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.5848 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.8501 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -4.0356 |
| sortino_ratio | -1.3103 |
| max_drawdown | 0.8039 |
| cagr | -0.4653 |
| net_avg_win | 46.9836 |
| net_avg_loss | -64.5950 |
| avg_hold_time_bars | 29.9157 |
| exposure | 0.7230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
