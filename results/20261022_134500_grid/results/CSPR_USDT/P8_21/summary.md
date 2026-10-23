# EMA Hourly Continuation — CSPR/USDT P8_21

**Symbol:** CSPR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1873 |
| net_profit_factor | 0.2639 |
| net_win_rate | 0.3812 |
| gross_profit_factor | 0.7012 |
| gross_win_rate | 0.4095 |
| sharpe_ratio | -14.7825 |
| sortino_ratio | -9.0690 |
| max_drawdown | 1.0000 |
| cagr | -0.9898 |
| net_avg_win | 5.0211 |
| net_avg_loss | -11.7213 |
| avg_hold_time_bars | 2.6401 |
| exposure | 0.2248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
