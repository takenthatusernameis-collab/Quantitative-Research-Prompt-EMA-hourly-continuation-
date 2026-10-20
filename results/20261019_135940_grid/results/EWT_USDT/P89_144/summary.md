# EMA Hourly Continuation — EWT/USDT P89_144

**Symbol:** EWT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.3941 |
| net_win_rate | 0.3881 |
| gross_profit_factor | 0.6548 |
| gross_win_rate | 0.3963 |
| sharpe_ratio | -6.3795 |
| sortino_ratio | -1.9891 |
| max_drawdown | 0.9210 |
| cagr | -0.6254 |
| net_avg_win | 31.4856 |
| net_avg_loss | -50.6760 |
| avg_hold_time_bars | 5.3368 |
| exposure | 0.1181 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
