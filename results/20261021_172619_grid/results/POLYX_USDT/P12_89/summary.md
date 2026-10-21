# EMA Hourly Continuation — POLYX/USDT P12_89

**Symbol:** POLYX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 561 |
| net_profit_factor | 0.8742 |
| net_win_rate | 0.5258 |
| gross_profit_factor | 1.1100 |
| gross_win_rate | 0.5258 |
| sharpe_ratio | -1.0767 |
| sortino_ratio | -0.3667 |
| max_drawdown | 0.4363 |
| cagr | -0.1585 |
| net_avg_win | 82.8379 |
| net_avg_loss | -105.0932 |
| avg_hold_time_bars | 20.6132 |
| exposure | 0.5256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
