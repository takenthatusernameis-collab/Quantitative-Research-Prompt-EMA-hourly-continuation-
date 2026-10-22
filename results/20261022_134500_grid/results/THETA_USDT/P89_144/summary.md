# EMA Hourly Continuation — THETA/USDT P89_144

**Symbol:** THETA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.4641 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8401 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -4.7222 |
| sortino_ratio | -1.5011 |
| max_drawdown | 0.8392 |
| cagr | -0.5160 |
| net_avg_win | 31.5722 |
| net_avg_loss | -56.6863 |
| avg_hold_time_bars | 4.5375 |
| exposure | 0.1044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
