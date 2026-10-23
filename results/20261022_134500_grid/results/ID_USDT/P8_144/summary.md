# EMA Hourly Continuation — ID/USDT P8_144

**Symbol:** ID/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6945 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 0.9581 |
| gross_win_rate | 0.4957 |
| sharpe_ratio | -2.2426 |
| sortino_ratio | -0.6787 |
| max_drawdown | 0.5705 |
| cagr | -0.2773 |
| net_avg_win | 55.5211 |
| net_avg_loss | -77.2429 |
| avg_hold_time_bars | 35.9528 |
| exposure | 0.7582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
