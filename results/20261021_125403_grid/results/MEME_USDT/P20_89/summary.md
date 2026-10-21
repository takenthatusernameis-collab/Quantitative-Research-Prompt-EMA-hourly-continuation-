# EMA Hourly Continuation — MEME/USDT P20_89

**Symbol:** MEME/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.8208 |
| net_win_rate | 0.5030 |
| gross_profit_factor | 1.0193 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -1.5256 |
| sortino_ratio | -0.4920 |
| max_drawdown | 0.5029 |
| cagr | -0.2044 |
| net_avg_win | 78.4569 |
| net_avg_loss | -96.7277 |
| avg_hold_time_bars | 17.4142 |
| exposure | 0.4013 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
