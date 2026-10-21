# EMA Hourly Continuation — VET/USDT P12_200

**Symbol:** VET/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.8081 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9807 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.1030 |
| sortino_ratio | -0.2711 |
| max_drawdown | 0.3708 |
| cagr | -0.1184 |
| net_avg_win | 77.1986 |
| net_avg_loss | -95.5331 |
| avg_hold_time_bars | 56.1216 |
| exposure | 0.7551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
