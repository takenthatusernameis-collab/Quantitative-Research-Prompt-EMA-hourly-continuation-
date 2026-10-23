# EMA Hourly Continuation — DEGEN/USDT P20_26

**Symbol:** DEGEN/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1151 |
| net_profit_factor | 0.4273 |
| net_win_rate | 0.3979 |
| gross_profit_factor | 0.7865 |
| gross_win_rate | 0.4240 |
| sharpe_ratio | -10.9759 |
| sortino_ratio | -5.2821 |
| max_drawdown | 0.9989 |
| cagr | -0.9333 |
| net_avg_win | 16.2751 |
| net_avg_loss | -25.1699 |
| avg_hold_time_bars | 2.3710 |
| exposure | 0.1242 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
