# EMA Hourly Continuation — AKT/USDT P12_100

**Symbol:** AKT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.8301 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 0.9787 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -1.2844 |
| sortino_ratio | -0.4009 |
| max_drawdown | 0.4091 |
| cagr | -0.1711 |
| net_avg_win | 77.7892 |
| net_avg_loss | -91.7671 |
| avg_hold_time_bars | 24.0084 |
| exposure | 0.5205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
