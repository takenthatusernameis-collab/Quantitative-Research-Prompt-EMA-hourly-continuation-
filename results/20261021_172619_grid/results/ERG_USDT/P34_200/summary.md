# EMA Hourly Continuation — ERG/USDT P34_200

**Symbol:** ERG/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.6863 |
| net_win_rate | 0.4611 |
| gross_profit_factor | 0.8388 |
| gross_win_rate | 0.4611 |
| sharpe_ratio | -2.0435 |
| sortino_ratio | -0.5302 |
| max_drawdown | 0.4737 |
| cagr | -0.2170 |
| net_avg_win | 65.2053 |
| net_avg_loss | -81.2853 |
| avg_hold_time_bars | 29.2485 |
| exposure | 0.4440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
