# EMA Hourly Continuation — WEMIX/USDT P55_144

**Symbol:** WEMIX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 819 |
| net_profit_factor | 0.3300 |
| net_win_rate | 0.3089 |
| gross_profit_factor | 0.5306 |
| gross_win_rate | 0.3162 |
| sharpe_ratio | -11.4120 |
| sortino_ratio | -4.6403 |
| max_drawdown | 0.9977 |
| cagr | -0.9100 |
| net_avg_win | 19.4219 |
| net_avg_loss | -26.3076 |
| avg_hold_time_bars | 7.9231 |
| exposure | 0.2950 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
