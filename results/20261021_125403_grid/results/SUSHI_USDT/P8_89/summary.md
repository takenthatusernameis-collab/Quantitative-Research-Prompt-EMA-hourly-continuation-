# EMA Hourly Continuation — SUSHI/USDT P8_89

**Symbol:** SUSHI/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.7064 |
| net_win_rate | 0.4630 |
| gross_profit_factor | 0.8673 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -2.5795 |
| sortino_ratio | -0.8394 |
| max_drawdown | 0.6462 |
| cagr | -0.3209 |
| net_avg_win | 61.4514 |
| net_avg_loss | -75.0066 |
| avg_hold_time_bars | 26.0569 |
| exposure | 0.6214 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
