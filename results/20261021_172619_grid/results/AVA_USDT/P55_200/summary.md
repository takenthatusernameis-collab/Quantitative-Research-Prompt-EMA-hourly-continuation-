# EMA Hourly Continuation — AVA/USDT P55_200

**Symbol:** AVA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.9949 |
| net_win_rate | 0.5509 |
| gross_profit_factor | 1.2202 |
| gross_win_rate | 0.5509 |
| sharpe_ratio | 0.0270 |
| sortino_ratio | 0.0066 |
| max_drawdown | 0.2079 |
| cagr | -0.0028 |
| net_avg_win | 85.7582 |
| net_avg_loss | -105.7320 |
| avg_hold_time_bars | 26.8877 |
| exposure | 0.3483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
