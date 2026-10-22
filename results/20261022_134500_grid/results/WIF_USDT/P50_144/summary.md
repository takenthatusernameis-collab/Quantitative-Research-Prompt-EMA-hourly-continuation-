# EMA Hourly Continuation — WIF/USDT P50_144

**Symbol:** WIF/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.6342 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9121 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -3.0745 |
| sortino_ratio | -0.9690 |
| max_drawdown | 0.6963 |
| cagr | -0.3682 |
| net_avg_win | 49.6383 |
| net_avg_loss | -71.9526 |
| avg_hold_time_bars | 11.6333 |
| exposure | 0.2639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
