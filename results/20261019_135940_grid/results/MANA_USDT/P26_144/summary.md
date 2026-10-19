# EMA Hourly Continuation — MANA/USDT P26_144

**Symbol:** MANA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.6078 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.9605 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -3.9199 |
| sortino_ratio | -1.2007 |
| max_drawdown | 0.7860 |
| cagr | -0.4509 |
| net_avg_win | 53.3588 |
| net_avg_loss | -76.6003 |
| avg_hold_time_bars | 22.4907 |
| exposure | 0.4958 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
