# EMA Hourly Continuation — LQTY/USDT P89_200

**Symbol:** LQTY/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.6591 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 0.9244 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -2.4759 |
| sortino_ratio | -0.6980 |
| max_drawdown | 0.5596 |
| cagr | -0.2758 |
| net_avg_win | 56.6766 |
| net_avg_loss | -80.0865 |
| avg_hold_time_bars | 11.1345 |
| exposure | 0.1985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
