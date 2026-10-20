# EMA Hourly Continuation — ARKM/USDT P8_144

**Symbol:** ARKM/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.6538 |
| net_win_rate | 0.4619 |
| gross_profit_factor | 0.8886 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -3.0068 |
| sortino_ratio | -0.9177 |
| max_drawdown | 0.6894 |
| cagr | -0.3543 |
| net_avg_win | 57.7532 |
| net_avg_loss | -75.8152 |
| avg_hold_time_bars | 36.1059 |
| exposure | 0.7746 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
