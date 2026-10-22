# EMA Hourly Continuation — HBAR/USDT P21_89

**Symbol:** HBAR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 746 |
| net_profit_factor | 0.5637 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.9403 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -4.8123 |
| sortino_ratio | -1.8546 |
| max_drawdown | 0.8964 |
| cagr | -0.5903 |
| net_avg_win | 32.5202 |
| net_avg_loss | -52.3812 |
| avg_hold_time_bars | 10.3338 |
| exposure | 0.3504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
