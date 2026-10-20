# EMA Hourly Continuation — DIA/USDT P8_20

**Symbol:** DIA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1576 |
| net_profit_factor | 0.3071 |
| net_win_rate | 0.4270 |
| gross_profit_factor | 0.6874 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -11.1198 |
| sortino_ratio | -6.2071 |
| max_drawdown | 0.9996 |
| cagr | -0.9549 |
| net_avg_win | 6.5821 |
| net_avg_loss | -15.9753 |
| avg_hold_time_bars | 3.3173 |
| exposure | 0.2366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
