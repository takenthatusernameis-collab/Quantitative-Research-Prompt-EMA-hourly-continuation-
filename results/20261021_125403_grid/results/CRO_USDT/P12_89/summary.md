# EMA Hourly Continuation — CRO/USDT P12_89

**Symbol:** CRO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.7631 |
| net_win_rate | 0.5135 |
| gross_profit_factor | 1.0413 |
| gross_win_rate | 0.5135 |
| sharpe_ratio | -1.8349 |
| sortino_ratio | -0.5999 |
| max_drawdown | 0.5302 |
| cagr | -0.2406 |
| net_avg_win | 60.4515 |
| net_avg_loss | -83.6152 |
| avg_hold_time_bars | 21.3456 |
| exposure | 0.5026 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
