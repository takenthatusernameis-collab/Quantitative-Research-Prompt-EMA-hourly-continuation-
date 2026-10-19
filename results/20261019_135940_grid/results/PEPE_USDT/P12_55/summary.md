# EMA Hourly Continuation — PEPE/USDT P12_55

**Symbol:** PEPE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1021 |
| net_profit_factor | 0.6520 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 1.0043 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -5.4435 |
| sortino_ratio | -2.4484 |
| max_drawdown | 0.9505 |
| cagr | -0.6931 |
| net_avg_win | 36.2755 |
| net_avg_loss | -51.3375 |
| avg_hold_time_bars | 7.8237 |
| exposure | 0.3631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
