# EMA Hourly Continuation — KSM/USDT P100_144

**Symbol:** KSM/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.4721 |
| net_win_rate | 0.4558 |
| gross_profit_factor | 0.9382 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -5.5159 |
| sortino_ratio | -1.7475 |
| max_drawdown | 0.8839 |
| cagr | -0.5741 |
| net_avg_win | 34.7855 |
| net_avg_loss | -61.7127 |
| avg_hold_time_bars | 4.0241 |
| exposure | 0.0911 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
