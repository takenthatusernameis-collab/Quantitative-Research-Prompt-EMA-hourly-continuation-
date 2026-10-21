# EMA Hourly Continuation — ATH/USDT P12_89

**Symbol:** ATH/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.8994 |
| net_win_rate | 0.5213 |
| gross_profit_factor | 1.0735 |
| gross_win_rate | 0.5213 |
| sharpe_ratio | -0.6921 |
| sortino_ratio | -0.2282 |
| max_drawdown | 0.3008 |
| cagr | -0.1046 |
| net_avg_win | 79.7070 |
| net_avg_loss | -96.5084 |
| avg_hold_time_bars | 20.5456 |
| exposure | 0.4910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
