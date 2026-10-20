# EMA Hourly Continuation — EWT/USDT P21_144

**Symbol:** EWT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.4980 |
| net_win_rate | 0.4168 |
| gross_profit_factor | 0.7296 |
| gross_win_rate | 0.4220 |
| sharpe_ratio | -5.0915 |
| sortino_ratio | -1.7045 |
| max_drawdown | 0.8938 |
| cagr | -0.5690 |
| net_avg_win | 35.8880 |
| net_avg_loss | -51.5078 |
| avg_hold_time_bars | 16.0823 |
| exposure | 0.4262 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
