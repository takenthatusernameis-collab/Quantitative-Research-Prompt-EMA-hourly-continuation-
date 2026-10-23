# EMA Hourly Continuation — ASTR/USDT P50_144

**Symbol:** ASTR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.6207 |
| net_win_rate | 0.4848 |
| gross_profit_factor | 0.9770 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -3.3053 |
| sortino_ratio | -1.0017 |
| max_drawdown | 0.7173 |
| cagr | -0.3788 |
| net_avg_win | 51.2899 |
| net_avg_loss | -77.7571 |
| avg_hold_time_bars | 13.4565 |
| exposure | 0.2801 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
