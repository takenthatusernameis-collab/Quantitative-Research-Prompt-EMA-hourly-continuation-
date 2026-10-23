# EMA Hourly Continuation — SYN/USDT P26_89

**Symbol:** SYN/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.6219 |
| net_win_rate | 0.4684 |
| gross_profit_factor | 0.9182 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -4.0775 |
| sortino_ratio | -1.5144 |
| max_drawdown | 0.8465 |
| cagr | -0.5163 |
| net_avg_win | 42.3185 |
| net_avg_loss | -59.9512 |
| avg_hold_time_bars | 10.7011 |
| exposure | 0.3385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
