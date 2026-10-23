# EMA Hourly Continuation — MOVR/USDT P26_144

**Symbol:** MOVR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 577 |
| net_profit_factor | 0.5447 |
| net_win_rate | 0.4523 |
| gross_profit_factor | 0.8321 |
| gross_win_rate | 0.4679 |
| sharpe_ratio | -3.9622 |
| sortino_ratio | -1.3331 |
| max_drawdown | 0.8112 |
| cagr | -0.4719 |
| net_avg_win | 36.6090 |
| net_avg_loss | -55.5165 |
| avg_hold_time_bars | 16.8336 |
| exposure | 0.4415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
