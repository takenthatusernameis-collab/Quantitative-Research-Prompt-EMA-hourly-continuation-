# EMA Hourly Continuation — RLC/USDT P89_100

**Symbol:** RLC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 174 |
| net_profit_factor | 0.8071 |
| net_win_rate | 0.5632 |
| gross_profit_factor | 1.2725 |
| gross_win_rate | 0.5632 |
| sharpe_ratio | -0.8242 |
| sortino_ratio | -0.1573 |
| max_drawdown | 0.2033 |
| cagr | -0.0704 |
| net_avg_win | 71.5294 |
| net_avg_loss | -114.2860 |
| avg_hold_time_bars | 4.1437 |
| exposure | 0.0328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
