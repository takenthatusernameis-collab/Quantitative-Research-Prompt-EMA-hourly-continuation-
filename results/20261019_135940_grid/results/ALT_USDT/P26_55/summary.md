# EMA Hourly Continuation — ALT/USDT P26_55

**Symbol:** ALT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 807 |
| net_profit_factor | 0.5161 |
| net_win_rate | 0.4374 |
| gross_profit_factor | 0.8379 |
| gross_win_rate | 0.4449 |
| sharpe_ratio | -6.2308 |
| sortino_ratio | -2.4995 |
| max_drawdown | 0.9533 |
| cagr | -0.6983 |
| net_avg_win | 28.7278 |
| net_avg_loss | -43.2769 |
| avg_hold_time_bars | 5.7893 |
| exposure | 0.2124 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
