# EMA Hourly Continuation — ETHFI/USDT P8_89

**Symbol:** ETHFI/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 728 |
| net_profit_factor | 0.6294 |
| net_win_rate | 0.4574 |
| gross_profit_factor | 0.8750 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -4.0371 |
| sortino_ratio | -1.5336 |
| max_drawdown | 0.8470 |
| cagr | -0.5171 |
| net_avg_win | 42.8028 |
| net_avg_loss | -57.3326 |
| avg_hold_time_bars | 19.1319 |
| exposure | 0.6331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
