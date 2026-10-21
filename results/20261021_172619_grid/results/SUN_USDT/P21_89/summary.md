# EMA Hourly Continuation — SUN/USDT P21_89

**Symbol:** SUN/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.5084 |
| net_win_rate | 0.4165 |
| gross_profit_factor | 0.8091 |
| gross_win_rate | 0.4334 |
| sharpe_ratio | -5.4625 |
| sortino_ratio | -1.6821 |
| max_drawdown | 0.8712 |
| cagr | -0.5519 |
| net_avg_win | 45.5613 |
| net_avg_loss | -63.9703 |
| avg_hold_time_bars | 17.9175 |
| exposure | 0.3835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
