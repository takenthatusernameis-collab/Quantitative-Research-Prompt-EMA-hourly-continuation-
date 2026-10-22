# EMA Hourly Continuation — INJ/USDT P12_144

**Symbol:** INJ/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.5870 |
| net_win_rate | 0.4399 |
| gross_profit_factor | 0.7857 |
| gross_win_rate | 0.4399 |
| sharpe_ratio | -3.6317 |
| sortino_ratio | -1.0998 |
| max_drawdown | 0.7348 |
| cagr | -0.4078 |
| net_avg_win | 50.7229 |
| net_avg_loss | -67.8738 |
| avg_hold_time_bars | 33.0107 |
| exposure | 0.6992 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
