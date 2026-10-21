# EMA Hourly Continuation — ZEC/USDT P12_89

**Symbol:** ZEC/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.9870 |
| net_win_rate | 0.5393 |
| gross_profit_factor | 1.1591 |
| gross_win_rate | 0.5393 |
| sharpe_ratio | -0.0226 |
| sortino_ratio | -0.0070 |
| max_drawdown | 0.2671 |
| cagr | -0.0121 |
| net_avg_win | 92.3659 |
| net_avg_loss | -109.5476 |
| avg_hold_time_bars | 24.8231 |
| exposure | 0.5168 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
