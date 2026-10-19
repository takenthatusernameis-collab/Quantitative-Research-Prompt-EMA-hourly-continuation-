# EMA Hourly Continuation — TRX/USDT P21_55

**Symbol:** TRX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 808 |
| net_profit_factor | 0.2136 |
| net_win_rate | 0.3713 |
| gross_profit_factor | 0.8551 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -12.3828 |
| sortino_ratio | -5.1948 |
| max_drawdown | 0.9992 |
| cagr | -0.9423 |
| net_avg_win | 9.0494 |
| net_avg_loss | -25.0139 |
| avg_hold_time_bars | 5.5817 |
| exposure | 0.2050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
