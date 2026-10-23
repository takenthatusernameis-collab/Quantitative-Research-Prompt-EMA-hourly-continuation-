# EMA Hourly Continuation — XCH/USDT P12_89

**Symbol:** XCH/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 835 |
| net_profit_factor | 0.5872 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.9483 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -4.5480 |
| sortino_ratio | -1.8522 |
| max_drawdown | 0.8928 |
| cagr | -0.5857 |
| net_avg_win | 32.3189 |
| net_avg_loss | -48.7018 |
| avg_hold_time_bars | 14.9521 |
| exposure | 0.5675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
