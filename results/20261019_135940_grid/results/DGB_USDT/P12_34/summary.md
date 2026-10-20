# EMA Hourly Continuation — DGB/USDT P12_34

**Symbol:** DGB/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1439 |
| net_profit_factor | 0.4382 |
| net_win_rate | 0.4128 |
| gross_profit_factor | 0.8841 |
| gross_win_rate | 0.4322 |
| sharpe_ratio | -11.2142 |
| sortino_ratio | -5.9736 |
| max_drawdown | 0.9995 |
| cagr | -0.9517 |
| net_avg_win | 13.1261 |
| net_avg_loss | -21.0556 |
| avg_hold_time_bars | 3.7603 |
| exposure | 0.2460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
