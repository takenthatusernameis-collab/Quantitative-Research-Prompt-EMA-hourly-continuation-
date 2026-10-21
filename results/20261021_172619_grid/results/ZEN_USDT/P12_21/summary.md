# EMA Hourly Continuation — ZEN/USDT P12_21

**Symbol:** ZEN/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.6245 |
| net_win_rate | 0.4823 |
| gross_profit_factor | 0.9230 |
| gross_win_rate | 0.4823 |
| sharpe_ratio | -2.6994 |
| sortino_ratio | -0.7415 |
| max_drawdown | 0.5749 |
| cagr | -0.2876 |
| net_avg_win | 53.8588 |
| net_avg_loss | -80.3485 |
| avg_hold_time_bars | 4.9319 |
| exposure | 0.0823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
