# EMA Hourly Continuation — DEGEN/USDT P21_89

**Symbol:** DEGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.7406 |
| net_win_rate | 0.4912 |
| gross_profit_factor | 1.0047 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -2.9510 |
| sortino_ratio | -1.0872 |
| max_drawdown | 0.7468 |
| cagr | -0.4029 |
| net_avg_win | 62.0334 |
| net_avg_loss | -80.8512 |
| avg_hold_time_bars | 12.5912 |
| exposure | 0.3898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
