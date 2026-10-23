# EMA Hourly Continuation — MANTA/USDT P26_89

**Symbol:** MANTA/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.6374 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.9399 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -4.4113 |
| sortino_ratio | -1.6424 |
| max_drawdown | 0.8650 |
| cagr | -0.5447 |
| net_avg_win | 46.1739 |
| net_avg_loss | -63.5266 |
| avg_hold_time_bars | 10.0114 |
| exposure | 0.3195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
