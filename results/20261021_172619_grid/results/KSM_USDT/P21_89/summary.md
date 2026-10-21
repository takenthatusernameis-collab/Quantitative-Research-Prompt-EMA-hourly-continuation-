# EMA Hourly Continuation — KSM/USDT P21_89

**Symbol:** KSM/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.7145 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.9217 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -2.5217 |
| sortino_ratio | -0.7930 |
| max_drawdown | 0.6296 |
| cagr | -0.3057 |
| net_avg_win | 64.7320 |
| net_avg_loss | -82.4220 |
| avg_hold_time_bars | 17.1027 |
| exposure | 0.3786 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
