# EMA Hourly Continuation — MEME/USDT P100_144

**Symbol:** MEME/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.8103 |
| net_win_rate | 0.5252 |
| gross_profit_factor | 1.0825 |
| gross_win_rate | 0.5252 |
| sharpe_ratio | -1.0142 |
| sortino_ratio | -0.2439 |
| max_drawdown | 0.3197 |
| cagr | -0.1069 |
| net_avg_win | 72.3032 |
| net_avg_loss | -98.6920 |
| avg_hold_time_bars | 7.1475 |
| exposure | 0.0903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
