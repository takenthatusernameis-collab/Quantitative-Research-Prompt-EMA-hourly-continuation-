# EMA Hourly Continuation — HBAR/USDT P12_50

**Symbol:** HBAR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.7951 |
| net_win_rate | 0.5156 |
| gross_profit_factor | 1.0620 |
| gross_win_rate | 0.5156 |
| sharpe_ratio | -1.9025 |
| sortino_ratio | -0.6936 |
| max_drawdown | 0.5690 |
| cagr | -0.2724 |
| net_avg_win | 64.4772 |
| net_avg_loss | -86.3091 |
| avg_hold_time_bars | 9.5109 |
| exposure | 0.2775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
