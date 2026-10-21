# EMA Hourly Continuation — JTO/USDT P50_55

**Symbol:** JTO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 143 |
| net_profit_factor | 0.6081 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8389 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -1.8716 |
| sortino_ratio | -0.3193 |
| max_drawdown | 0.3204 |
| cagr | -0.1364 |
| net_avg_win | 73.5604 |
| net_avg_loss | -100.8050 |
| avg_hold_time_bars | 4.9161 |
| exposure | 0.0320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
