# EMA Hourly Continuation — LISTA/USDT P34_200

**Symbol:** LISTA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.6668 |
| net_win_rate | 0.4628 |
| gross_profit_factor | 0.8772 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -2.4992 |
| sortino_ratio | -0.7110 |
| max_drawdown | 0.5403 |
| cagr | -0.2832 |
| net_avg_win | 62.1539 |
| net_avg_loss | -80.2860 |
| avg_hold_time_bars | 26.4362 |
| exposure | 0.4860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
