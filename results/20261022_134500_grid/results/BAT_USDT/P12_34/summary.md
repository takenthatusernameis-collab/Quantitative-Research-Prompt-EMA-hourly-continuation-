# EMA Hourly Continuation — BAT/USDT P12_34

**Symbol:** BAT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1248 |
| net_profit_factor | 0.3764 |
| net_win_rate | 0.4399 |
| gross_profit_factor | 0.8476 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -8.8668 |
| sortino_ratio | -4.4250 |
| max_drawdown | 0.9957 |
| cagr | -0.8849 |
| net_avg_win | 10.9484 |
| net_avg_loss | -22.8424 |
| avg_hold_time_bars | 4.4159 |
| exposure | 0.2505 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
