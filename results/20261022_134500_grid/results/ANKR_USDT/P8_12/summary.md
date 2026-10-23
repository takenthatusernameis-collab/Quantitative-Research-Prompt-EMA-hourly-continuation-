# EMA Hourly Continuation — ANKR/USDT P8_12

**Symbol:** ANKR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1807 |
| net_profit_factor | 0.1891 |
| net_win_rate | 0.3520 |
| gross_profit_factor | 0.6155 |
| gross_win_rate | 0.4200 |
| sharpe_ratio | -18.6347 |
| sortino_ratio | -11.6066 |
| max_drawdown | 1.0000 |
| cagr | -0.9978 |
| net_avg_win | 3.6674 |
| net_avg_loss | -10.5315 |
| avg_hold_time_bars | 2.1400 |
| exposure | 0.1758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
