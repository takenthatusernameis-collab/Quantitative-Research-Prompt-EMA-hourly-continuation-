# EMA Hourly Continuation — ADA/USDT P8_34

**Symbol:** ADA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1402 |
| net_profit_factor | 0.4613 |
| net_win_rate | 0.4408 |
| gross_profit_factor | 0.9626 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -9.6764 |
| sortino_ratio | -5.0853 |
| max_drawdown | 0.9984 |
| cagr | -0.9220 |
| net_avg_win | 13.8335 |
| net_avg_loss | -23.6385 |
| avg_hold_time_bars | 4.9180 |
| exposure | 0.3134 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
