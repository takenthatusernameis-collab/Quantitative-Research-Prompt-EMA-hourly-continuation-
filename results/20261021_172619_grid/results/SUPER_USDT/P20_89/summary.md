# EMA Hourly Continuation — SUPER/USDT P20_89

**Symbol:** SUPER/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.8866 |
| net_win_rate | 0.5310 |
| gross_profit_factor | 1.1162 |
| gross_win_rate | 0.5310 |
| sharpe_ratio | -0.7829 |
| sortino_ratio | -0.2565 |
| max_drawdown | 0.3159 |
| cagr | -0.1152 |
| net_avg_win | 75.4844 |
| net_avg_loss | -96.3999 |
| avg_hold_time_bars | 15.9845 |
| exposure | 0.3749 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
