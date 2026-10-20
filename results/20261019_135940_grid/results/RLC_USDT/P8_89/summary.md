# EMA Hourly Continuation — RLC/USDT P8_89

**Symbol:** RLC/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.7856 |
| net_win_rate | 0.5205 |
| gross_profit_factor | 1.1579 |
| gross_win_rate | 0.5287 |
| sharpe_ratio | -2.2477 |
| sortino_ratio | -0.7798 |
| max_drawdown | 0.6846 |
| cagr | -0.3145 |
| net_avg_win | 70.8014 |
| net_avg_loss | -97.8443 |
| avg_hold_time_bars | 24.7455 |
| exposure | 0.6850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
