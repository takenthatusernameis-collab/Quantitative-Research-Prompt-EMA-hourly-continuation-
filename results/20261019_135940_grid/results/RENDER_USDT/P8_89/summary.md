# EMA Hourly Continuation — RENDER/USDT P8_89

**Symbol:** RENDER/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.6504 |
| net_win_rate | 0.4786 |
| gross_profit_factor | 0.9071 |
| gross_win_rate | 0.4849 |
| sharpe_ratio | -3.4937 |
| sortino_ratio | -1.3301 |
| max_drawdown | 0.7534 |
| cagr | -0.4696 |
| net_avg_win | 45.9811 |
| net_avg_loss | -64.8911 |
| avg_hold_time_bars | 19.2472 |
| exposure | 0.6410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
