# EMA Hourly Continuation — TFUEL/USDT P26_100

**Symbol:** TFUEL/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.5660 |
| net_win_rate | 0.4137 |
| gross_profit_factor | 0.7412 |
| gross_win_rate | 0.4137 |
| sharpe_ratio | -4.6333 |
| sortino_ratio | -1.5425 |
| max_drawdown | 0.8370 |
| cagr | -0.5095 |
| net_avg_win | 47.3088 |
| net_avg_loss | -58.9660 |
| avg_hold_time_bars | 12.1133 |
| exposure | 0.3048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
