# EMA Hourly Continuation — SEI/USDT P8_12

**Symbol:** SEI/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1818 |
| net_profit_factor | 0.2565 |
| net_win_rate | 0.3597 |
| gross_profit_factor | 0.7089 |
| gross_win_rate | 0.4065 |
| sharpe_ratio | -17.9866 |
| sortino_ratio | -11.1220 |
| max_drawdown | 1.0000 |
| cagr | -0.9973 |
| net_avg_win | 5.2752 |
| net_avg_loss | -11.5550 |
| avg_hold_time_bars | 1.7959 |
| exposure | 0.1484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
