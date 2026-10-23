# EMA Hourly Continuation — UQC/USDT P26_144

**Symbol:** UQC/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.3527 |
| net_win_rate | 0.3216 |
| gross_profit_factor | 0.4752 |
| gross_win_rate | 0.3216 |
| sharpe_ratio | -4.7126 |
| sortino_ratio | -0.9884 |
| max_drawdown | 0.7050 |
| cagr | -0.3837 |
| net_avg_win | 52.6240 |
| net_avg_loss | -70.7275 |
| avg_hold_time_bars | 65.3612 |
| exposure | 0.6715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
