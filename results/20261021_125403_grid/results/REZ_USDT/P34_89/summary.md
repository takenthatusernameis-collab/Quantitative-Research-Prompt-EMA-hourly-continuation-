# EMA Hourly Continuation — REZ/USDT P34_89

**Symbol:** REZ/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.9120 |
| net_win_rate | 0.5303 |
| gross_profit_factor | 1.1192 |
| gross_win_rate | 0.5303 |
| sharpe_ratio | -0.5945 |
| sortino_ratio | -0.1858 |
| max_drawdown | 0.3286 |
| cagr | -0.0867 |
| net_avg_win | 85.0151 |
| net_avg_loss | -105.2461 |
| avg_hold_time_bars | 12.0866 |
| exposure | 0.2576 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
