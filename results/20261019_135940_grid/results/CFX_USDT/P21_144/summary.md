# EMA Hourly Continuation — CFX/USDT P21_144

**Symbol:** CFX/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.6720 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 0.9698 |
| gross_win_rate | 0.4960 |
| sharpe_ratio | -2.7763 |
| sortino_ratio | -0.8707 |
| max_drawdown | 0.6740 |
| cagr | -0.3410 |
| net_avg_win | 54.2909 |
| net_avg_loss | -77.0144 |
| avg_hold_time_bars | 22.4721 |
| exposure | 0.5128 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
