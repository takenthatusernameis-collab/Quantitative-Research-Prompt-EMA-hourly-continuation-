# EMA Hourly Continuation — AIOZ/USDT P12_100

**Symbol:** AIOZ/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 773 |
| net_profit_factor | 0.6671 |
| net_win_rate | 0.4605 |
| gross_profit_factor | 0.9148 |
| gross_win_rate | 0.4631 |
| sharpe_ratio | -4.5200 |
| sortino_ratio | -1.7696 |
| max_drawdown | 0.8813 |
| cagr | -0.5701 |
| net_avg_win | 49.5304 |
| net_avg_loss | -63.3876 |
| avg_hold_time_bars | 16.0880 |
| exposure | 0.5653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
