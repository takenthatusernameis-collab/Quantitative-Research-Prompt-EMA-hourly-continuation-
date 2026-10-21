# EMA Hourly Continuation — CETUS/USDT P12_144

**Symbol:** CETUS/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 1.1172 |
| net_win_rate | 0.5658 |
| gross_profit_factor | 1.2941 |
| gross_win_rate | 0.5658 |
| sharpe_ratio | 0.6656 |
| sortino_ratio | 0.1692 |
| max_drawdown | 0.1831 |
| cagr | 0.0693 |
| net_avg_win | 102.0781 |
| net_avg_loss | -119.0537 |
| avg_hold_time_bars | 53.9211 |
| exposure | 0.7418 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
