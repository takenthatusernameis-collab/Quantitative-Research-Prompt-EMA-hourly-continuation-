# EMA Hourly Continuation — RSR/USDT P21_26

**Symbol:** RSR/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1159 |
| net_profit_factor | 0.2847 |
| net_win_rate | 0.3857 |
| gross_profit_factor | 0.7965 |
| gross_win_rate | 0.4193 |
| sharpe_ratio | -12.6669 |
| sortino_ratio | -6.2067 |
| max_drawdown | 0.9997 |
| cagr | -0.9611 |
| net_avg_win | 8.9031 |
| net_avg_loss | -19.6303 |
| avg_hold_time_bars | 1.9456 |
| exposure | 0.1025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
