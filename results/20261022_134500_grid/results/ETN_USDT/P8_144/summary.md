# EMA Hourly Continuation — ETN/USDT P8_144

**Symbol:** ETN/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.4817 |
| net_win_rate | 0.4026 |
| gross_profit_factor | 0.6725 |
| gross_win_rate | 0.4128 |
| sharpe_ratio | -6.6622 |
| sortino_ratio | -2.6649 |
| max_drawdown | 0.9372 |
| cagr | -0.7259 |
| net_avg_win | 31.3371 |
| net_avg_loss | -43.8476 |
| avg_hold_time_bars | 16.0334 |
| exposure | 0.5992 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
