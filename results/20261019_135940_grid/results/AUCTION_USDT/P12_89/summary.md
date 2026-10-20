# EMA Hourly Continuation — AUCTION/USDT P12_89

**Symbol:** AUCTION/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.6308 |
| net_win_rate | 0.4669 |
| gross_profit_factor | 0.9347 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -4.2921 |
| sortino_ratio | -1.5351 |
| max_drawdown | 0.8496 |
| cagr | -0.5207 |
| net_avg_win | 47.5639 |
| net_avg_loss | -66.0311 |
| avg_hold_time_bars | 19.4730 |
| exposure | 0.5720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
