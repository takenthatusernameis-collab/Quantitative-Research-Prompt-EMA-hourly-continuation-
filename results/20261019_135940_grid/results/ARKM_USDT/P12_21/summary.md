# EMA Hourly Continuation — ARKM/USDT P12_21

**Symbol:** ARKM/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1517 |
| net_profit_factor | 0.3759 |
| net_win_rate | 0.3975 |
| gross_profit_factor | 0.7150 |
| gross_win_rate | 0.4166 |
| sharpe_ratio | -12.8635 |
| sortino_ratio | -7.0864 |
| max_drawdown | 0.9999 |
| cagr | -0.9727 |
| net_avg_win | 9.9860 |
| net_avg_loss | -17.5277 |
| avg_hold_time_bars | 2.2149 |
| exposure | 0.1527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
