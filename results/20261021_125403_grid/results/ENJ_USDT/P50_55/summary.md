# EMA Hourly Continuation — ENJ/USDT P50_55

**Symbol:** ENJ/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 127 |
| net_profit_factor | 0.5709 |
| net_win_rate | 0.4567 |
| gross_profit_factor | 0.8478 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -2.0084 |
| sortino_ratio | -0.3232 |
| max_drawdown | 0.3220 |
| cagr | -0.1397 |
| net_avg_win | 72.4469 |
| net_avg_loss | -106.6606 |
| avg_hold_time_bars | 4.1102 |
| exposure | 0.0236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
