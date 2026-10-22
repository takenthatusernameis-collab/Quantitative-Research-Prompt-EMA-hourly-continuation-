# EMA Hourly Continuation — SNX/USDT P55_144

**Symbol:** SNX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.7074 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0872 |
| gross_win_rate | 0.5155 |
| sharpe_ratio | -2.5675 |
| sortino_ratio | -0.7973 |
| max_drawdown | 0.6214 |
| cagr | -0.3153 |
| net_avg_win | 60.9788 |
| net_avg_loss | -88.0042 |
| avg_hold_time_bars | 11.0228 |
| exposure | 0.2409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
