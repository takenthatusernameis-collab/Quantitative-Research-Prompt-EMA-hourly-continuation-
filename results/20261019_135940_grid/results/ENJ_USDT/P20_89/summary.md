# EMA Hourly Continuation — ENJ/USDT P20_89

**Symbol:** ENJ/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.6123 |
| net_win_rate | 0.4590 |
| gross_profit_factor | 0.9643 |
| gross_win_rate | 0.4729 |
| sharpe_ratio | -4.8532 |
| sortino_ratio | -1.8315 |
| max_drawdown | 0.8988 |
| cagr | -0.5848 |
| net_avg_win | 42.6025 |
| net_avg_loss | -59.0212 |
| avg_hold_time_bars | 12.0223 |
| exposure | 0.3929 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
