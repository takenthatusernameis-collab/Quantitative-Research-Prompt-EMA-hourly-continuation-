# EMA Hourly Continuation — LQTY/USDT P34_144

**Symbol:** LQTY/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.6531 |
| net_win_rate | 0.4786 |
| gross_profit_factor | 0.9061 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -2.7993 |
| sortino_ratio | -0.9010 |
| max_drawdown | 0.6605 |
| cagr | -0.3395 |
| net_avg_win | 49.6544 |
| net_avg_loss | -69.7851 |
| avg_hold_time_bars | 17.6634 |
| exposure | 0.4108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
