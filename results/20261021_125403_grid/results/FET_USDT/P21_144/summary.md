# EMA Hourly Continuation — FET/USDT P21_144

**Symbol:** FET/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.8757 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0060 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -0.6508 |
| sortino_ratio | -0.1676 |
| max_drawdown | 0.2504 |
| cagr | -0.0770 |
| net_avg_win | 78.7827 |
| net_avg_loss | -91.6507 |
| avg_hold_time_bars | 38.5356 |
| exposure | 0.5658 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
