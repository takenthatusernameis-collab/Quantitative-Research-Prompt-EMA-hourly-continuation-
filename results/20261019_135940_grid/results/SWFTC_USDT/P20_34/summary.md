# EMA Hourly Continuation — SWFTC/USDT P20_34

**Symbol:** SWFTC/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1071 |
| net_profit_factor | 0.2470 |
| net_win_rate | 0.3585 |
| gross_profit_factor | 0.5890 |
| gross_win_rate | 0.3763 |
| sharpe_ratio | -12.6743 |
| sortino_ratio | -5.9076 |
| max_drawdown | 0.9996 |
| cagr | -0.9557 |
| net_avg_win | 8.5408 |
| net_avg_loss | -19.3241 |
| avg_hold_time_bars | 2.9804 |
| exposure | 0.1451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
