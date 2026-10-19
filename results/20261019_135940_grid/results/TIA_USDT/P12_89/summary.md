# EMA Hourly Continuation — TIA/USDT P12_89

**Symbol:** TIA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.7685 |
| net_win_rate | 0.5061 |
| gross_profit_factor | 1.0513 |
| gross_win_rate | 0.5122 |
| sharpe_ratio | -2.2998 |
| sortino_ratio | -0.8313 |
| max_drawdown | 0.6456 |
| cagr | -0.3259 |
| net_avg_win | 63.0525 |
| net_avg_loss | -84.0746 |
| avg_hold_time_bars | 18.2722 |
| exposure | 0.5432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
