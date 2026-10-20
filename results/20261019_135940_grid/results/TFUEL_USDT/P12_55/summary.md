# EMA Hourly Continuation — TFUEL/USDT P12_55

**Symbol:** TFUEL/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1213 |
| net_profit_factor | 0.4449 |
| net_win_rate | 0.3957 |
| gross_profit_factor | 0.7415 |
| gross_win_rate | 0.4106 |
| sharpe_ratio | -10.0455 |
| sortino_ratio | -4.9030 |
| max_drawdown | 0.9978 |
| cagr | -0.9118 |
| net_avg_win | 16.6634 |
| net_avg_loss | -24.5246 |
| avg_hold_time_bars | 6.6546 |
| exposure | 0.3653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
