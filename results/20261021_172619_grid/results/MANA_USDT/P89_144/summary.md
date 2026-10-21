# EMA Hourly Continuation — MANA/USDT P89_144

**Symbol:** MANA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.6061 |
| net_win_rate | 0.4567 |
| gross_profit_factor | 0.8340 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -2.6463 |
| sortino_ratio | -0.6423 |
| max_drawdown | 0.5417 |
| cagr | -0.2557 |
| net_avg_win | 61.0406 |
| net_avg_loss | -84.6780 |
| avg_hold_time_bars | 6.4394 |
| exposure | 0.0846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
