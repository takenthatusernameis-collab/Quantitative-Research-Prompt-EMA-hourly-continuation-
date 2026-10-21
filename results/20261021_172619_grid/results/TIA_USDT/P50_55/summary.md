# EMA Hourly Continuation — TIA/USDT P50_55

**Symbol:** TIA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 93 |
| net_profit_factor | 0.9255 |
| net_win_rate | 0.5484 |
| gross_profit_factor | 1.2035 |
| gross_win_rate | 0.5484 |
| sharpe_ratio | -0.2051 |
| sortino_ratio | -0.0287 |
| max_drawdown | 0.0951 |
| cagr | -0.0142 |
| net_avg_win | 85.7648 |
| net_avg_loss | -112.5274 |
| avg_hold_time_bars | 7.3763 |
| exposure | 0.0312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
