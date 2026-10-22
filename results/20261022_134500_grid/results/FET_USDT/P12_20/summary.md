# EMA Hourly Continuation — FET/USDT P12_20

**Symbol:** FET/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1546 |
| net_profit_factor | 0.3622 |
| net_win_rate | 0.4017 |
| gross_profit_factor | 0.7590 |
| gross_win_rate | 0.4282 |
| sharpe_ratio | -13.2723 |
| sortino_ratio | -7.4293 |
| max_drawdown | 0.9999 |
| cagr | -0.9778 |
| net_avg_win | 9.1430 |
| net_avg_loss | -16.9482 |
| avg_hold_time_bars | 1.9929 |
| exposure | 0.1400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
