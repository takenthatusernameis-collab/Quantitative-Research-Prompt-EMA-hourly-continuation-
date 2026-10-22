# EMA Hourly Continuation — HBAR/USDT P8_21

**Symbol:** HBAR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1753 |
| net_profit_factor | 0.3204 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.7831 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -12.0669 |
| sortino_ratio | -7.1197 |
| max_drawdown | 0.9999 |
| cagr | -0.9738 |
| net_avg_win | 5.9233 |
| net_avg_loss | -15.3750 |
| avg_hold_time_bars | 2.7096 |
| exposure | 0.2159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
