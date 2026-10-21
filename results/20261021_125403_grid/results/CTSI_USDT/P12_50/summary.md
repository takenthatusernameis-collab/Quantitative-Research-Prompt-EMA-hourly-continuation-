# EMA Hourly Continuation — CTSI/USDT P12_50

**Symbol:** CTSI/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 717 |
| net_profit_factor | 0.6821 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.9025 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -3.8438 |
| sortino_ratio | -1.4656 |
| max_drawdown | 0.8189 |
| cagr | -0.4898 |
| net_avg_win | 53.1802 |
| net_avg_loss | -66.1100 |
| avg_hold_time_bars | 9.7057 |
| exposure | 0.3163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
