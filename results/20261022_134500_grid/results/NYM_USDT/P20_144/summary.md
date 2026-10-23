# EMA Hourly Continuation — NYM/USDT P20_144

**Symbol:** NYM/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.3712 |
| net_win_rate | 0.3703 |
| gross_profit_factor | 0.6407 |
| gross_win_rate | 0.3870 |
| sharpe_ratio | -6.6649 |
| sortino_ratio | -2.0481 |
| max_drawdown | 0.9239 |
| cagr | -0.6402 |
| net_avg_win | 30.7914 |
| net_avg_loss | -48.7795 |
| avg_hold_time_bars | 24.5941 |
| exposure | 0.5344 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
