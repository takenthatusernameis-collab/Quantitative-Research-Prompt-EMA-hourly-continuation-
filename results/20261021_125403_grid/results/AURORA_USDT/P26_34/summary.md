# EMA Hourly Continuation — AURORA/USDT P26_34

**Symbol:** AURORA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 0.4265 |
| net_win_rate | 0.4274 |
| gross_profit_factor | 0.7512 |
| gross_win_rate | 0.4274 |
| sharpe_ratio | -4.1616 |
| sortino_ratio | -0.9330 |
| max_drawdown | 0.6911 |
| cagr | -0.3591 |
| net_avg_win | 48.5863 |
| net_avg_loss | -85.0186 |
| avg_hold_time_bars | 7.7303 |
| exposure | 0.0847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
