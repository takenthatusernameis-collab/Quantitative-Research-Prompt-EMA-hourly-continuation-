# EMA Hourly Continuation — SEI/USDT P12_144

**Symbol:** SEI/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.9806 |
| net_win_rate | 0.5372 |
| gross_profit_factor | 1.1440 |
| gross_win_rate | 0.5372 |
| sharpe_ratio | -0.0557 |
| sortino_ratio | -0.0138 |
| max_drawdown | 0.2103 |
| cagr | -0.0119 |
| net_avg_win | 93.6761 |
| net_avg_loss | -110.8754 |
| avg_hold_time_bars | 53.4797 |
| exposure | 0.7195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
