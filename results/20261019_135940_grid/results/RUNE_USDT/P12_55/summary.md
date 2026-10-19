# EMA Hourly Continuation — RUNE/USDT P12_55

**Symbol:** RUNE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 843 |
| net_profit_factor | 0.6273 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 1.0716 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -4.7763 |
| sortino_ratio | -1.9382 |
| max_drawdown | 0.9115 |
| cagr | -0.6146 |
| net_avg_win | 36.5907 |
| net_avg_loss | -57.3703 |
| avg_hold_time_bars | 12.0652 |
| exposure | 0.4623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
