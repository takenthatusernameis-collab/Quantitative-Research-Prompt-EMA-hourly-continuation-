# EMA Hourly Continuation — NEAR/USDT P12_89

**Symbol:** NEAR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.7373 |
| net_win_rate | 0.4717 |
| gross_profit_factor | 0.8737 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -1.9408 |
| sortino_ratio | -0.5919 |
| max_drawdown | 0.5289 |
| cagr | -0.2396 |
| net_avg_win | 64.3138 |
| net_avg_loss | -77.8998 |
| avg_hold_time_bars | 26.3391 |
| exposure | 0.5507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
