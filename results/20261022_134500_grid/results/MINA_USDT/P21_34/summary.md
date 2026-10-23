# EMA Hourly Continuation — MINA/USDT P21_34

**Symbol:** MINA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1155 |
| net_profit_factor | 0.3835 |
| net_win_rate | 0.4277 |
| gross_profit_factor | 0.9130 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -9.9928 |
| sortino_ratio | -4.8470 |
| max_drawdown | 0.9975 |
| cagr | -0.9073 |
| net_avg_win | 12.5580 |
| net_avg_loss | -24.4753 |
| avg_hold_time_bars | 2.9948 |
| exposure | 0.1572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
