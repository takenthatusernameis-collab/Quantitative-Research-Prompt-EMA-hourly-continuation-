# EMA Hourly Continuation — ARB/USDT P20_144

**Symbol:** ARB/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.7062 |
| net_win_rate | 0.4955 |
| gross_profit_factor | 1.0221 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -2.4810 |
| sortino_ratio | -0.7422 |
| max_drawdown | 0.5946 |
| cagr | -0.2968 |
| net_avg_win | 63.5425 |
| net_avg_loss | -88.3914 |
| avg_hold_time_bars | 28.4286 |
| exposure | 0.5789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
