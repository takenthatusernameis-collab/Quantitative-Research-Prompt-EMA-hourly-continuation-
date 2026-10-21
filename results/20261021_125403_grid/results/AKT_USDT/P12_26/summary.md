# EMA Hourly Continuation — AKT/USDT P12_26

**Symbol:** AKT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.7467 |
| net_win_rate | 0.5039 |
| gross_profit_factor | 0.9892 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -1.6515 |
| sortino_ratio | -0.4678 |
| max_drawdown | 0.4971 |
| cagr | -0.1932 |
| net_avg_win | 62.6884 |
| net_avg_loss | -85.2579 |
| avg_hold_time_bars | 5.2853 |
| exposure | 0.0935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
