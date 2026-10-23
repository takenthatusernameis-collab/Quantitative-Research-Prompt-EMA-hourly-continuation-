# EMA Hourly Continuation — ATH/USDT P8_144

**Symbol:** ATH/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.8025 |
| net_win_rate | 0.5211 |
| gross_profit_factor | 1.1091 |
| gross_win_rate | 0.5282 |
| sharpe_ratio | -1.4846 |
| sortino_ratio | -0.4442 |
| max_drawdown | 0.4522 |
| cagr | -0.1944 |
| net_avg_win | 73.0084 |
| net_avg_loss | -99.0087 |
| avg_hold_time_bars | 37.3732 |
| exposure | 0.7717 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
