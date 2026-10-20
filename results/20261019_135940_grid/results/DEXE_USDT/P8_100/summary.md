# EMA Hourly Continuation — DEXE/USDT P8_100

**Symbol:** DEXE/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.6674 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 0.9555 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -2.7504 |
| sortino_ratio | -0.9374 |
| max_drawdown | 0.7103 |
| cagr | -0.3644 |
| net_avg_win | 46.7075 |
| net_avg_loss | -68.5709 |
| avg_hold_time_bars | 26.7305 |
| exposure | 0.7169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
