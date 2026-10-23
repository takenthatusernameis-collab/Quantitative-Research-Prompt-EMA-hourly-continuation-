# EMA Hourly Continuation — WIN/USDT P12_89

**Symbol:** WIN/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.5071 |
| net_win_rate | 0.4644 |
| gross_profit_factor | 0.9129 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -5.3080 |
| sortino_ratio | -1.9348 |
| max_drawdown | 0.9120 |
| cagr | -0.6173 |
| net_avg_win | 29.9265 |
| net_avg_loss | -51.1659 |
| avg_hold_time_bars | 18.3264 |
| exposure | 0.5615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
