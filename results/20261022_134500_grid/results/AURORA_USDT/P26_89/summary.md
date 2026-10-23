# EMA Hourly Continuation — AURORA/USDT P26_89

**Symbol:** AURORA/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.5718 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.9613 |
| gross_win_rate | 0.4710 |
| sharpe_ratio | -4.9303 |
| sortino_ratio | -1.6686 |
| max_drawdown | 0.8752 |
| cagr | -0.5600 |
| net_avg_win | 43.6469 |
| net_avg_loss | -63.8909 |
| avg_hold_time_bars | 11.8447 |
| exposure | 0.3155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
