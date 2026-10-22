# EMA Hourly Continuation — UQC/USDT P8_100

**Symbol:** UQC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 247 |
| net_profit_factor | 0.3678 |
| net_win_rate | 0.2955 |
| gross_profit_factor | 0.5159 |
| gross_win_rate | 0.3117 |
| sharpe_ratio | -5.7624 |
| sortino_ratio | -1.2494 |
| max_drawdown | 0.8105 |
| cagr | -0.4798 |
| net_avg_win | 64.3680 |
| net_avg_loss | -73.4202 |
| avg_hold_time_bars | 63.4130 |
| exposure | 0.7089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
