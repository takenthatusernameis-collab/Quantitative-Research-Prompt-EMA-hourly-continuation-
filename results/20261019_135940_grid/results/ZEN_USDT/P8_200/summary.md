# EMA Hourly Continuation — ZEN/USDT P8_200

**Symbol:** ZEN/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 145 |
| net_profit_factor | 0.9702 |
| net_win_rate | 0.5517 |
| gross_profit_factor | 1.2298 |
| gross_win_rate | 0.5517 |
| sharpe_ratio | -0.0714 |
| sortino_ratio | -0.0122 |
| max_drawdown | 0.1230 |
| cagr | -0.0086 |
| net_avg_win | 86.9946 |
| net_avg_loss | -110.3587 |
| avg_hold_time_bars | 138.3448 |
| exposure | 0.9118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
