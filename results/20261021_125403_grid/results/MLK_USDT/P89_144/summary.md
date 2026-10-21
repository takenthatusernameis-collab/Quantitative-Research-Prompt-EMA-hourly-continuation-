# EMA Hourly Continuation — MLK/USDT P89_144

**Symbol:** MLK/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.3856 |
| net_win_rate | 0.3466 |
| gross_profit_factor | 0.5493 |
| gross_win_rate | 0.3466 |
| sharpe_ratio | -4.7139 |
| sortino_ratio | -1.0597 |
| max_drawdown | 0.7176 |
| cagr | -0.3921 |
| net_avg_win | 51.5834 |
| net_avg_loss | -70.9687 |
| avg_hold_time_bars | 7.9602 |
| exposure | 0.0904 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
