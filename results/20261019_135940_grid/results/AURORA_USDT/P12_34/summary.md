# EMA Hourly Continuation — AURORA/USDT P12_34

**Symbol:** AURORA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1055 |
| net_profit_factor | 0.4059 |
| net_win_rate | 0.3886 |
| gross_profit_factor | 0.8484 |
| gross_win_rate | 0.4161 |
| sharpe_ratio | -10.8688 |
| sortino_ratio | -4.9957 |
| max_drawdown | 0.9987 |
| cagr | -0.9260 |
| net_avg_win | 16.6372 |
| net_avg_loss | -26.0570 |
| avg_hold_time_bars | 5.5175 |
| exposure | 0.2646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
