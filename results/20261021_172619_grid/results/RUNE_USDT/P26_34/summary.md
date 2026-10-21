# EMA Hourly Continuation — RUNE/USDT P26_34

**Symbol:** RUNE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 198 |
| net_profit_factor | 0.7770 |
| net_win_rate | 0.5354 |
| gross_profit_factor | 1.1616 |
| gross_win_rate | 0.5354 |
| sharpe_ratio | -1.1401 |
| sortino_ratio | -0.2321 |
| max_drawdown | 0.2680 |
| cagr | -0.1007 |
| net_avg_win | 76.8863 |
| net_avg_loss | -114.0158 |
| avg_hold_time_bars | 4.4141 |
| exposure | 0.0397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
